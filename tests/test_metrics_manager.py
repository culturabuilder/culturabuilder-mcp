"""
Tests for MetricsManager functionality
"""

import unittest
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from setup.managers.metrics_manager import MetricsManager, ExportFormat


class TestMetricsManager(unittest.TestCase):
    """Test suite for MetricsManager"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = Path(tempfile.mkdtemp())
        self.metrics_manager = MetricsManager(self.test_dir)
        # Enable metrics for testing
        self.metrics_manager.metrics_enabled = True
    
    def tearDown(self):
        """Clean up test environment"""
        shutil.rmtree(self.test_dir)
    
    def test_initialization(self):
        """Test MetricsManager initialization"""
        self.assertTrue(self.metrics_manager.metrics_file.exists())
        self.assertEqual(self.metrics_manager.metrics_file.name, ".culturabuilder-metrics.json")
        
        # Check initial structure
        metrics = self.metrics_manager._load_metrics()
        self.assertIn("version", metrics)
        self.assertIn("privacy", metrics)
        self.assertIn("usage", metrics)
        self.assertIn("performance", metrics)
        self.assertIn("errors", metrics)
    
    def test_privacy_controls(self):
        """Test privacy enable/disable functionality"""
        # Initially disabled
        self.metrics_manager.metrics_enabled = False
        self.assertFalse(self.metrics_manager._check_metrics_consent())
        
        # Enable metrics
        self.assertTrue(self.metrics_manager.enable_metrics(anonymous=True))
        metrics = self.metrics_manager._load_metrics()
        self.assertTrue(metrics["privacy"]["enabled"])
        self.assertTrue(metrics["privacy"]["anonymous"])
        
        # Disable metrics
        self.assertTrue(self.metrics_manager.disable_metrics())
        metrics = self.metrics_manager._load_metrics()
        self.assertFalse(metrics["privacy"]["enabled"])
    
    def test_record_command(self):
        """Test command recording functionality"""
        self.metrics_manager.record_command(
            command="install",
            flags=["--verbose", "--dry-run"],
            success=True,
            duration=2.5,
            metadata={"components": 3}
        )
        
        metrics = self.metrics_manager._load_metrics()
        
        # Check command was recorded
        self.assertIn("install", metrics["usage"]["commands"])
        install_data = metrics["usage"]["commands"]["install"]
        self.assertEqual(install_data["count"], 1)
        self.assertEqual(install_data["success"], 1)
        self.assertEqual(install_data["failed"], 0)
        self.assertEqual(install_data["total_duration"], 2.5)
        
        # Check flags were recorded
        self.assertIn("--verbose", metrics["usage"]["flags"])
        self.assertIn("--dry-run", metrics["usage"]["flags"])
        self.assertEqual(metrics["usage"]["flags"]["--verbose"]["count"], 1)
        
        # Check performance record
        self.assertEqual(len(metrics["performance"]["operations"]), 1)
        operation = metrics["performance"]["operations"][0]
        self.assertEqual(operation["command"], "install")
        self.assertEqual(operation["flags"], ["--verbose", "--dry-run"])
        self.assertTrue(operation["success"])
        self.assertEqual(operation["duration"], 2.5)
        self.assertIn("metadata", operation)
    
    def test_record_component_usage(self):
        """Test component usage recording"""
        self.metrics_manager.record_component_usage("Commands", "install")
        self.metrics_manager.record_component_usage("Commands", "use")
        self.metrics_manager.record_component_usage("Core", "update")
        
        metrics = self.metrics_manager._load_metrics()
        
        self.assertIn("Commands", metrics["usage"]["components"])
        self.assertIn("Core", metrics["usage"]["components"])
        
        commands_data = metrics["usage"]["components"]["Commands"]
        self.assertEqual(commands_data["install_count"], 1)
        self.assertEqual(commands_data["use_count"], 1)
        self.assertIsNotNone(commands_data["last_used"])
        
        core_data = metrics["usage"]["components"]["Core"]
        self.assertEqual(core_data["update_count"], 1)
    
    def test_record_error(self):
        """Test error recording"""
        self.metrics_manager.record_error(
            error_type="FileNotFoundError",
            command="install",
            details="Config file missing"
        )
        
        self.metrics_manager.record_error(
            error_type="PermissionError",
            command="update",
            details="Access denied"
        )
        
        metrics = self.metrics_manager._load_metrics()
        
        # Check error types
        self.assertEqual(metrics["errors"]["by_type"]["FileNotFoundError"], 1)
        self.assertEqual(metrics["errors"]["by_type"]["PermissionError"], 1)
        
        # Check errors by command
        self.assertIn("install", metrics["errors"]["by_command"])
        self.assertEqual(metrics["errors"]["by_command"]["install"]["FileNotFoundError"], 1)
        
        # Check recent errors
        self.assertEqual(len(metrics["errors"]["recent"]), 2)
        recent = metrics["errors"]["recent"][0]
        self.assertEqual(recent["type"], "FileNotFoundError")
        self.assertEqual(recent["command"], "install")
        self.assertEqual(recent["details"], "Config file missing")
    
    def test_session_tracking(self):
        """Test session start and end tracking"""
        session_id = self.metrics_manager.session_id
        self.assertIsNotNone(session_id)
        self.assertTrue(session_id.startswith("session_"))
        
        # Record session end
        self.metrics_manager.record_session_end()
        
        metrics = self.metrics_manager._load_metrics()
        self.assertEqual(len(metrics["usage"]["sessions"]), 1)
        
        session = metrics["usage"]["sessions"][0]
        self.assertEqual(session["id"], session_id)
        self.assertIn("start", session)
        self.assertIn("end", session)
        self.assertIn("duration", session)
        self.assertGreater(session["duration"], 0)
    
    def test_summary_stats(self):
        """Test summary statistics generation"""
        # Record some test data
        self.metrics_manager.record_command("install", ["--verbose"], True, 2.0)
        self.metrics_manager.record_command("update", [], True, 3.0)
        self.metrics_manager.record_command("install", ["--force"], False, 1.5)
        self.metrics_manager.record_error("TestError", "install", "Test")
        
        summary = self.metrics_manager.get_summary_stats()
        
        self.assertEqual(summary["total_commands"], 3)
        self.assertEqual(summary["unique_commands"], 2)
        self.assertEqual(summary["total_errors"], 1)
        self.assertEqual(summary["error_types"], 1)
        
        # Check performance metrics
        self.assertIn("performance", summary)
        perf = summary["performance"]
        self.assertAlmostEqual(perf["duration"], 2.17, places=1)
        self.assertAlmostEqual(perf["success_rate"], 0.67, places=1)
        
        # Check top commands
        self.assertIn("top_commands", summary)
        self.assertEqual(summary["top_commands"][0]["name"], "install")
        self.assertEqual(summary["top_commands"][0]["count"], 2)
    
    def test_time_series_data(self):
        """Test time series data generation"""
        # Record operations at different times
        now = datetime.now()
        
        # Mock operations with different timestamps
        metrics = self.metrics_manager._load_metrics()
        metrics["performance"]["operations"] = [
            {
                "timestamp": now.isoformat(),
                "command": "install",
                "flags": [],
                "success": True,
                "duration": 2.0,
                "session_id": "test"
            },
            {
                "timestamp": (now - timedelta(hours=1)).isoformat(),
                "command": "update",
                "flags": [],
                "success": False,
                "duration": 3.0,
                "session_id": "test"
            },
            {
                "timestamp": (now - timedelta(days=1)).isoformat(),
                "command": "install",
                "flags": [],
                "success": True,
                "duration": 1.5,
                "session_id": "test"
            }
        ]
        self.metrics_manager._save_metrics(metrics)
        
        # Test hourly aggregation
        hourly = self.metrics_manager.get_time_series_data("hour")
        self.assertIn("periods", hourly)
        self.assertIn("data", hourly)
        self.assertGreater(len(hourly["periods"]), 0)
        
        # Test daily aggregation
        daily = self.metrics_manager.get_time_series_data("day")
        self.assertGreater(len(daily["periods"]), 0)
        self.assertEqual(len(daily["data"]["operations"]), len(daily["periods"]))
    
    def test_export_json(self):
        """Test JSON export functionality"""
        # Add test data
        self.metrics_manager.record_command("test", [], True, 1.0)
        
        output_path = self.test_dir / "test_export.json"
        result = self.metrics_manager.export_metrics(
            format=ExportFormat.JSON,
            output_path=output_path
        )
        
        self.assertEqual(result, output_path)
        self.assertTrue(output_path.exists())
        
        # Verify exported data
        with open(output_path, 'r') as f:
            exported = json.load(f)
        
        self.assertIn("usage", exported)
        self.assertIn("performance", exported)
        self.assertIn("test", exported["usage"]["commands"])
    
    def test_export_csv(self):
        """Test CSV export functionality"""
        # Add test data
        self.metrics_manager.record_command("install", ["--verbose"], True, 2.0)
        self.metrics_manager.record_command("update", [], False, 3.0)
        
        output_path = self.test_dir / "test_export.csv"
        result = self.metrics_manager.export_metrics(
            format=ExportFormat.CSV,
            output_path=output_path
        )
        
        # CSV export creates multiple files
        commands_file = self.test_dir / "test_export_commands.csv"
        self.assertTrue(commands_file.exists())
        
        # Verify CSV content
        with open(commands_file, 'r') as f:
            content = f.read()
            self.assertIn("install", content)
            self.assertIn("update", content)
    
    def test_export_html(self):
        """Test HTML export functionality"""
        # Add test data
        self.metrics_manager.record_command("install", [], True, 1.5)
        
        output_path = self.test_dir / "test_export.html"
        result = self.metrics_manager.export_metrics(
            format=ExportFormat.HTML,
            output_path=output_path
        )
        
        self.assertEqual(result, output_path)
        self.assertTrue(output_path.exists())
        
        # Verify HTML content
        with open(output_path, 'r') as f:
            content = f.read()
            self.assertIn("<html>", content)
            self.assertIn("CulturaBuilder Metrics Report", content)
            self.assertIn("install", content)
    
    def test_export_markdown(self):
        """Test Markdown export functionality"""
        # Add test data
        self.metrics_manager.record_command("test", [], True, 2.0)
        
        output_path = self.test_dir / "test_export.md"
        result = self.metrics_manager.export_metrics(
            format=ExportFormat.MARKDOWN,
            output_path=output_path
        )
        
        self.assertEqual(result, output_path)
        self.assertTrue(output_path.exists())
        
        # Verify Markdown content
        with open(output_path, 'r') as f:
            content = f.read()
            self.assertIn("# CulturaBuilder Metrics Report", content)
            self.assertIn("## Summary Statistics", content)
            self.assertIn("test", content)
    
    def test_time_range_filtering(self):
        """Test filtering metrics by time range"""
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        week_ago = now - timedelta(days=7)
        
        # Create test data with different timestamps
        metrics = self.metrics_manager._load_metrics()
        metrics["performance"]["operations"] = [
            {"timestamp": now.isoformat(), "command": "recent", "flags": [], 
             "success": True, "duration": 1.0, "session_id": "test"},
            {"timestamp": yesterday.isoformat(), "command": "yesterday", "flags": [], 
             "success": True, "duration": 1.0, "session_id": "test"},
            {"timestamp": week_ago.isoformat(), "command": "old", "flags": [], 
             "success": True, "duration": 1.0, "session_id": "test"}
        ]
        self.metrics_manager._save_metrics(metrics)
        
        # Test filtering
        filtered = self.metrics_manager._filter_by_time_range(
            metrics, 
            yesterday - timedelta(hours=1),
            now + timedelta(hours=1)
        )
        
        # Should only include recent and yesterday
        self.assertEqual(len(filtered["performance"]["operations"]), 2)
        commands = [op["command"] for op in filtered["performance"]["operations"]]
        self.assertIn("recent", commands)
        self.assertIn("yesterday", commands)
        self.assertNotIn("old", commands)
    
    def test_clear_metrics(self):
        """Test clearing metrics data"""
        # Add some data
        self.metrics_manager.record_command("test", [], True, 1.0)
        
        # Verify data exists
        metrics = self.metrics_manager._load_metrics()
        self.assertIn("test", metrics["usage"]["commands"])
        
        # Clear without confirmation should fail
        self.assertFalse(self.metrics_manager.clear_metrics(confirm=False))
        
        # Clear with confirmation
        self.assertTrue(self.metrics_manager.clear_metrics(confirm=True))
        
        # Verify data is cleared
        metrics = self.metrics_manager._load_metrics()
        self.assertEqual(len(metrics["usage"]["commands"]), 0)
        self.assertEqual(len(metrics["performance"]["operations"]), 0)
    
    def test_privacy_status(self):
        """Test privacy status reporting"""
        self.metrics_manager.enable_metrics(anonymous=True)
        
        status = self.metrics_manager.get_privacy_status()
        
        self.assertIn("enabled", status)
        self.assertIn("anonymous", status)
        self.assertIn("data_location", status)
        self.assertIn("data_size_kb", status)
        
        self.assertTrue(status["enabled"])
        self.assertTrue(status["anonymous"])
        self.assertEqual(status["data_location"], str(self.metrics_manager.metrics_file))
    
    def test_metrics_disabled_no_recording(self):
        """Test that metrics are not recorded when disabled"""
        self.metrics_manager.metrics_enabled = False
        
        # Try to record operations
        self.metrics_manager.record_command("test", [], True, 1.0)
        self.metrics_manager.record_component_usage("test", "install")
        self.metrics_manager.record_error("TestError", "test", "details")
        
        # Check nothing was recorded
        metrics = self.metrics_manager._load_metrics()
        self.assertEqual(len(metrics["usage"]["commands"]), 0)
        self.assertEqual(len(metrics["usage"]["components"]), 0)
        self.assertEqual(len(metrics["errors"]["by_type"]), 0)
    
    def test_performance_averages(self):
        """Test performance average calculations"""
        # Record multiple operations
        self.metrics_manager.record_command("install", [], True, 2.0)
        self.metrics_manager.record_command("install", [], True, 3.0)
        self.metrics_manager.record_command("install", [], False, 4.0)
        self.metrics_manager.record_command("update", [], True, 1.0)
        
        metrics = self.metrics_manager._load_metrics()
        averages = metrics["performance"]["averages"]
        
        # Overall averages
        self.assertAlmostEqual(averages["duration"], 2.5, places=1)
        self.assertAlmostEqual(averages["success_rate"], 0.75, places=2)
        self.assertEqual(averages["total_operations"], 4)
        
        # Per-command averages
        self.assertIn("by_command", averages)
        install_avg = averages["by_command"]["install"]
        self.assertAlmostEqual(install_avg["avg_duration"], 3.0, places=1)
        self.assertAlmostEqual(install_avg["success_rate"], 0.67, places=1)
        self.assertEqual(install_avg["total_count"], 3)


if __name__ == "__main__":
    unittest.main()