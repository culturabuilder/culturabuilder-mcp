"""
Metrics operations for SuperClaude Framework
Provides commands for viewing, managing, and exporting usage metrics
"""

import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

from ..utils.ui import (
    display_header, display_info, display_success, display_error,
    display_warning, prompt_yes_no, Colors
)
from ..utils.logger import get_logger
from ..managers.metrics_manager import MetricsManager, ExportFormat


def register_parser(subparsers, global_parser):
    """Register the metrics subcommand parser"""
    parser = subparsers.add_parser(
        'metrics',
        help='View and manage usage metrics',
        parents=[global_parser],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
Manage and view SuperClaude usage metrics

Privacy-respecting local analytics that help improve your workflow.
All data is stored locally and never transmitted.
        """,
        epilog="""
Examples:
  SuperClaude metrics --enable              # Enable metrics collection
  SuperClaude metrics --status              # View current metrics status
  SuperClaude metrics --summary              # Display summary statistics
  SuperClaude metrics --export html         # Export metrics as HTML report
  SuperClaude metrics --export csv --days 7 # Export last 7 days as CSV
  SuperClaude metrics --clear                # Clear all metrics data
        """
    )
    
    # Privacy controls
    privacy_group = parser.add_mutually_exclusive_group()
    privacy_group.add_argument('--enable', action='store_true',
                              help='Enable metrics collection (requires consent)')
    privacy_group.add_argument('--disable', action='store_true',
                              help='Disable metrics collection')
    privacy_group.add_argument('--status', action='store_true',
                              help='Show privacy settings and metrics status')
    
    # View options
    view_group = parser.add_argument_group('View Options')
    view_group.add_argument('--summary', action='store_true',
                           help='Display summary statistics')
    view_group.add_argument('--detailed', action='store_true',
                           help='Display detailed metrics')
    view_group.add_argument('--time-series', choices=['hour', 'day', 'week', 'month'],
                           help='Display time series data')
    view_group.add_argument('--top', type=int, default=10, metavar='N',
                           help='Number of top items to display (default: 10)')
    
    # Export options
    export_group = parser.add_argument_group('Export Options')
    export_group.add_argument('--export', choices=['json', 'csv', 'html', 'markdown'],
                             help='Export metrics to specified format')
    export_group.add_argument('--output', '-o', type=Path,
                             help='Output file path (auto-generated if not specified)')
    
    # Time range filters
    time_group = parser.add_argument_group('Time Filters')
    time_group.add_argument('--days', type=int,
                           help='Filter metrics to last N days')
    time_group.add_argument('--since', type=str,
                           help='Filter metrics since date (YYYY-MM-DD)')
    time_group.add_argument('--until', type=str,
                           help='Filter metrics until date (YYYY-MM-DD)')
    
    # Management options
    mgmt_group = parser.add_argument_group('Management')
    mgmt_group.add_argument('--clear', action='store_true',
                           help='Clear all metrics data (requires confirmation)')
    mgmt_group.add_argument('--anonymous', action='store_true',
                           help='Enable anonymous mode (no user-specific data)')


def run(args: argparse.Namespace) -> int:
    """Execute metrics operations"""
    logger = get_logger()
    
    try:
        # Initialize metrics manager
        metrics_manager = MetricsManager(args.install_dir)
        
        # Handle privacy controls first
        if args.enable:
            return handle_enable_metrics(metrics_manager, args)
        elif args.disable:
            return handle_disable_metrics(metrics_manager)
        elif args.status:
            return handle_status(metrics_manager)
        
        # Handle data management
        if args.clear:
            return handle_clear_metrics(metrics_manager, args)
        
        # Handle viewing options
        if args.summary:
            return handle_summary(metrics_manager, args)
        elif args.detailed:
            return handle_detailed(metrics_manager, args)
        elif args.time_series:
            return handle_time_series(metrics_manager, args)
        
        # Handle export
        if args.export:
            return handle_export(metrics_manager, args)
        
        # No specific action, show summary by default
        return handle_summary(metrics_manager, args)
        
    except Exception as e:
        display_error(f"Metrics operation failed: {e}")
        if logger:
            logger.exception("Metrics operation error")
        return 1


def handle_enable_metrics(metrics_manager: MetricsManager, args: argparse.Namespace) -> int:
    """Enable metrics collection with user consent"""
    display_header("Enable Metrics Collection", "Privacy-respecting local analytics")
    
    print(f"\n{Colors.CYAN}Privacy Notice:{Colors.RESET}")
    print("• All metrics are stored locally on your machine")
    print("• No data is ever transmitted over the network")
    print("• You can disable metrics at any time")
    print("• You can clear all data at any time")
    print("• Anonymous mode available (no user-specific data)")
    
    if not args.yes:
        if not prompt_yes_no("\nDo you consent to local metrics collection?"):
            display_info("Metrics collection not enabled")
            return 0
    
    anonymous = args.anonymous
    if not anonymous and not args.yes:
        anonymous = prompt_yes_no("Enable anonymous mode? (recommended)")
    
    if metrics_manager.enable_metrics(anonymous=anonymous):
        display_success("Metrics collection enabled")
        if anonymous:
            display_info("Anonymous mode: No user-specific data will be collected")
        return 0
    else:
        display_error("Failed to enable metrics")
        return 1


def handle_disable_metrics(metrics_manager: MetricsManager) -> int:
    """Disable metrics collection"""
    if metrics_manager.disable_metrics():
        display_success("Metrics collection disabled")
        display_info("Existing metrics data has been preserved")
        return 0
    else:
        display_error("Failed to disable metrics")
        return 1


def handle_status(metrics_manager: MetricsManager) -> int:
    """Display privacy settings and metrics status"""
    display_header("Metrics Status", "Privacy settings and data information")
    
    status = metrics_manager.get_privacy_status()
    
    print(f"\n{Colors.CYAN}Privacy Settings:{Colors.RESET}")
    print(f"  Collection enabled: {Colors.GREEN if status['enabled'] else Colors.RED}"
          f"{'Yes' if status['enabled'] else 'No'}{Colors.RESET}")
    print(f"  Anonymous mode: {'Yes' if status['anonymous'] else 'No'}")
    print(f"  Last consent check: {status['last_consent_check']}")
    
    print(f"\n{Colors.CYAN}Data Information:{Colors.RESET}")
    print(f"  Storage location: {status['data_location']}")
    print(f"  Data size: {status['data_size_kb']:.2f} KB")
    
    if status['enabled']:
        summary = metrics_manager.get_summary_stats()
        print(f"\n{Colors.CYAN}Collection Statistics:{Colors.RESET}")
        print(f"  Total commands: {summary['total_commands']}")
        print(f"  Unique commands: {summary['unique_commands']}")
        print(f"  Total sessions: {summary['total_sessions']}")
        print(f"  Success rate: {summary.get('performance', {}).get('success_rate', 0):.1%}")
    
    return 0


def handle_clear_metrics(metrics_manager: MetricsManager, args: argparse.Namespace) -> int:
    """Clear all metrics data"""
    display_warning("This will permanently delete all metrics data")
    
    if not args.yes:
        if not prompt_yes_no("Are you sure you want to clear all metrics?"):
            display_info("Clear operation cancelled")
            return 0
    
    if metrics_manager.clear_metrics(confirm=True):
        display_success("All metrics data cleared")
        return 0
    else:
        display_error("Failed to clear metrics")
        return 1


def handle_summary(metrics_manager: MetricsManager, args: argparse.Namespace) -> int:
    """Display summary statistics"""
    display_header("Metrics Summary", "Usage statistics overview")
    
    summary = metrics_manager.get_summary_stats()
    
    # Overall statistics
    print(f"\n{Colors.CYAN}Overall Statistics:{Colors.RESET}")
    print(f"  Total commands executed: {summary['total_commands']}")
    print(f"  Unique commands used: {summary['unique_commands']}")
    print(f"  Total flags used: {summary['total_flags_used']}")
    print(f"  Unique flags: {summary['unique_flags']}")
    print(f"  Total sessions: {summary['total_sessions']}")
    print(f"  Components used: {summary['components_used']}")
    
    # Performance metrics
    perf = summary.get('performance', {})
    if perf:
        print(f"\n{Colors.CYAN}Performance Metrics:{Colors.RESET}")
        print(f"  Average duration: {perf.get('duration', 0):.2f}s")
        print(f"  Success rate: {perf.get('success_rate', 0):.1%}")
        print(f"  Total operations: {perf.get('total_operations', 0)}")
    
    # Error statistics
    if summary['total_errors'] > 0:
        print(f"\n{Colors.CYAN}Error Statistics:{Colors.RESET}")
        print(f"  Total errors: {summary['total_errors']}")
        print(f"  Error types: {summary['error_types']}")
    
    # Top commands
    if 'top_commands' in summary and summary['top_commands']:
        print(f"\n{Colors.CYAN}Top Commands:{Colors.RESET}")
        for i, cmd in enumerate(summary['top_commands'][:args.top], 1):
            print(f"  {i}. {cmd['name']:<20} ({cmd['count']} uses)")
    
    # Top flags
    if 'top_flags' in summary and summary['top_flags']:
        print(f"\n{Colors.CYAN}Top Flags:{Colors.RESET}")
        for i, flag in enumerate(summary['top_flags'][:args.top], 1):
            print(f"  {i}. {flag['name']:<20} ({flag['count']} uses)")
    
    return 0


def handle_detailed(metrics_manager: MetricsManager, args: argparse.Namespace) -> int:
    """Display detailed metrics"""
    display_header("Detailed Metrics", "Comprehensive usage analysis")
    
    metrics = metrics_manager._load_metrics()
    
    # Commands detail
    print(f"\n{Colors.CYAN}Command Details:{Colors.RESET}")
    commands = sorted(metrics['usage']['commands'].items(), 
                     key=lambda x: x[1]['count'], reverse=True)
    
    for cmd, data in commands[:args.top]:
        success_rate = (data['success'] / data['count'] * 100) if data['count'] > 0 else 0
        avg_duration = (data['total_duration'] / data['count']) if data['count'] > 0 else 0
        
        print(f"\n  {Colors.GREEN}{cmd}{Colors.RESET}")
        print(f"    Total runs: {data['count']}")
        print(f"    Success: {data['success']} | Failed: {data['failed']}")
        print(f"    Success rate: {success_rate:.1f}%")
        print(f"    Avg duration: {avg_duration:.2f}s")
        
        if data['flags_used']:
            top_flags = sorted(data['flags_used'].items(), 
                             key=lambda x: x[1], reverse=True)[:3]
            print(f"    Top flags: {', '.join(f[0] for f in top_flags)}")
    
    # Component details
    if metrics['usage']['components']:
        print(f"\n{Colors.CYAN}Component Usage:{Colors.RESET}")
        components = sorted(metrics['usage']['components'].items(),
                          key=lambda x: x[1]['use_count'], reverse=True)
        
        for comp, data in components[:args.top]:
            print(f"\n  {Colors.GREEN}{comp}{Colors.RESET}")
            print(f"    Installs: {data['install_count']}")
            print(f"    Updates: {data['update_count']}")
            print(f"    Uses: {data['use_count']}")
            if data.get('last_used'):
                last_used = datetime.fromisoformat(data['last_used']).strftime('%Y-%m-%d %H:%M')
                print(f"    Last used: {last_used}")
    
    # Recent errors
    if metrics['errors']['recent']:
        print(f"\n{Colors.CYAN}Recent Errors:{Colors.RESET}")
        for error in metrics['errors']['recent'][-5:]:
            timestamp = datetime.fromisoformat(error['timestamp']).strftime('%Y-%m-%d %H:%M')
            print(f"\n  {Colors.RED}{error['type']}{Colors.RESET} at {timestamp}")
            if error.get('command'):
                print(f"    Command: {error['command']}")
            if error.get('details'):
                print(f"    Details: {error['details'][:100]}...")
    
    return 0


def handle_time_series(metrics_manager: MetricsManager, args: argparse.Namespace) -> int:
    """Display time series data"""
    display_header("Time Series Analysis", f"Metrics aggregated by {args.time_series}")
    
    time_data = metrics_manager.get_time_series_data(args.time_series)
    
    if not time_data['periods']:
        display_info("No time series data available")
        return 0
    
    print(f"\n{Colors.CYAN}Period: {time_data['period']}{Colors.RESET}")
    print(f"Data points: {len(time_data['periods'])}")
    
    # Display table header
    print(f"\n{'Period':<20} {'Operations':<12} {'Success Rate':<15} {'Avg Duration':<15}")
    print("-" * 62)
    
    # Display data
    for i, period in enumerate(time_data['periods']):
        # Format period for display
        dt = datetime.fromisoformat(period)
        if args.time_series == 'hour':
            period_str = dt.strftime('%Y-%m-%d %H:00')
        elif args.time_series == 'day':
            period_str = dt.strftime('%Y-%m-%d')
        elif args.time_series == 'week':
            period_str = f"Week of {dt.strftime('%Y-%m-%d')}"
        else:  # month
            period_str = dt.strftime('%Y-%m')
        
        ops = time_data['data']['operations'][i]
        success = time_data['data']['success_rate'][i]
        duration = time_data['data']['avg_duration'][i]
        
        # Color code success rate
        if success >= 95:
            success_color = Colors.GREEN
        elif success >= 80:
            success_color = Colors.YELLOW
        else:
            success_color = Colors.RED
        
        print(f"{period_str:<20} {ops:<12} "
              f"{success_color}{success:>6.1f}%{Colors.RESET}        "
              f"{duration:>8.2f}s")
    
    # Summary
    print("\n" + "-" * 62)
    total_ops = sum(time_data['data']['operations'])
    avg_success = sum(time_data['data']['success_rate']) / len(time_data['data']['success_rate'])
    avg_duration = sum(time_data['data']['avg_duration']) / len(time_data['data']['avg_duration'])
    
    print(f"{'TOTAL/AVERAGE':<20} {total_ops:<12} "
          f"{avg_success:>6.1f}%        {avg_duration:>8.2f}s")
    
    return 0


def handle_export(metrics_manager: MetricsManager, args: argparse.Namespace) -> int:
    """Export metrics to file"""
    display_header("Export Metrics", f"Exporting to {args.export.upper()} format")
    
    # Parse time range if specified
    time_range = None
    if args.days:
        end = datetime.now()
        start = end - timedelta(days=args.days)
        time_range = (start, end)
        display_info(f"Filtering to last {args.days} days")
    elif args.since or args.until:
        start = datetime.fromisoformat(args.since) if args.since else datetime.min
        end = datetime.fromisoformat(args.until) if args.until else datetime.now()
        time_range = (start, end)
        display_info(f"Filtering from {start.date()} to {end.date()}")
    
    # Determine export format
    format_map = {
        'json': ExportFormat.JSON,
        'csv': ExportFormat.CSV,
        'html': ExportFormat.HTML,
        'markdown': ExportFormat.MARKDOWN
    }
    export_format = format_map[args.export]
    
    # Export metrics
    try:
        output_path = metrics_manager.export_metrics(
            format=export_format,
            output_path=args.output,
            time_range=time_range
        )
        
        display_success(f"Metrics exported to: {output_path}")
        
        # Show file size
        file_size = output_path.stat().st_size
        if file_size < 1024:
            size_str = f"{file_size} bytes"
        elif file_size < 1024 * 1024:
            size_str = f"{file_size / 1024:.2f} KB"
        else:
            size_str = f"{file_size / (1024 * 1024):.2f} MB"
        
        display_info(f"File size: {size_str}")
        
        # For HTML exports, offer to open in browser
        if export_format == ExportFormat.HTML and not args.quiet:
            if prompt_yes_no("\nOpen in browser?"):
                import webbrowser
                webbrowser.open(f"file://{output_path.absolute()}")
        
        return 0
        
    except Exception as e:
        display_error(f"Export failed: {e}")
        return 1