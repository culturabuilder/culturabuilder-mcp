# SuperClaude Metrics Documentation

## Overview

SuperClaude includes a privacy-respecting, local-only usage metrics system that helps you understand and optimize your workflow. All metrics data is stored locally on your machine and is never transmitted over the network.

## Features

### 🔒 Privacy-First Design
- **100% Local Storage**: All data stays on your machine
- **No Network Transmission**: Metrics are never sent anywhere
- **Opt-In Only**: Explicitly requires your consent to enable
- **Anonymous Mode**: Option to collect only non-identifiable data
- **Full Control**: Enable, disable, or clear data at any time

### 📊 Comprehensive Tracking
- **Command Usage**: Track which commands you use most
- **Flag Patterns**: Understand your flag usage patterns
- **Performance Metrics**: Monitor execution times and success rates
- **Error Tracking**: Identify common issues and failure patterns
- **Component Usage**: Track which components are most valuable
- **Session Analytics**: Understand usage patterns over time

### 📈 Rich Analytics
- **Summary Statistics**: Quick overview of key metrics
- **Time Series Analysis**: View trends over time
- **Top Commands/Flags**: Identify your most-used features
- **Performance Trends**: Track improvements and regressions
- **Error Analysis**: Understand failure patterns

### 📤 Flexible Export
- **Multiple Formats**: JSON, CSV, HTML, Markdown
- **Time Range Filtering**: Export specific periods
- **Beautiful Reports**: HTML reports with charts and visualizations
- **Data Portability**: Easy to analyze in external tools

## Quick Start

### Enable Metrics Collection

```bash
# Enable with interactive consent
SuperClaude metrics --enable

# Enable with anonymous mode (recommended)
SuperClaude metrics --enable --anonymous

# Enable without prompts
SuperClaude metrics --enable --yes --anonymous
```

### View Metrics

```bash
# View summary statistics
SuperClaude metrics --summary

# View detailed metrics
SuperClaude metrics --detailed

# View time series data
SuperClaude metrics --time-series day

# Check privacy status
SuperClaude metrics --status
```

### Export Metrics

```bash
# Export as HTML report
SuperClaude metrics --export html

# Export last 7 days as CSV
SuperClaude metrics --export csv --days 7

# Export to specific file
SuperClaude metrics --export json --output ~/metrics.json

# Export with date range
SuperClaude metrics --export markdown --since 2025-01-01 --until 2025-01-31
```

### Manage Privacy

```bash
# Disable metrics collection
SuperClaude metrics --disable

# Clear all metrics data
SuperClaude metrics --clear

# Check current privacy settings
SuperClaude metrics --status
```

## Command Reference

### `SuperClaude metrics`

Main command for managing and viewing metrics.

#### Privacy Options

| Option | Description |
|--------|-------------|
| `--enable` | Enable metrics collection (requires consent) |
| `--disable` | Disable metrics collection |
| `--status` | Show privacy settings and metrics status |
| `--anonymous` | Enable anonymous mode (no user-specific data) |

#### View Options

| Option | Description |
|--------|-------------|
| `--summary` | Display summary statistics |
| `--detailed` | Display detailed metrics |
| `--time-series PERIOD` | Display time series data (hour/day/week/month) |
| `--top N` | Number of top items to display (default: 10) |

#### Export Options

| Option | Description |
|--------|-------------|
| `--export FORMAT` | Export metrics (json/csv/html/markdown) |
| `--output PATH` | Output file path (auto-generated if not specified) |

#### Time Filters

| Option | Description |
|--------|-------------|
| `--days N` | Filter metrics to last N days |
| `--since DATE` | Filter metrics since date (YYYY-MM-DD) |
| `--until DATE` | Filter metrics until date (YYYY-MM-DD) |

#### Management Options

| Option | Description |
|--------|-------------|
| `--clear` | Clear all metrics data (requires confirmation) |

## Data Schema

### Metrics Structure

```json
{
  "version": "1.0.0",
  "created_at": "ISO 8601 timestamp",
  "privacy": {
    "enabled": boolean,
    "anonymous": boolean,
    "last_consent_check": "ISO 8601 timestamp"
  },
  "usage": {
    "commands": {
      "command_name": {
        "count": number,
        "success": number,
        "failed": number,
        "total_duration": number,
        "flags_used": {}
      }
    },
    "flags": {
      "flag_name": {
        "count": number,
        "commands": {}
      }
    },
    "components": {
      "component_name": {
        "install_count": number,
        "update_count": number,
        "use_count": number,
        "last_used": "ISO 8601 timestamp"
      }
    },
    "sessions": [
      {
        "id": "session_id",
        "start": "ISO 8601 timestamp",
        "end": "ISO 8601 timestamp",
        "duration": number
      }
    ]
  },
  "performance": {
    "operations": [],
    "averages": {}
  },
  "errors": {
    "by_type": {},
    "by_command": {},
    "recent": []
  }
}
```

### Storage Location

Metrics are stored in `.superclaude-metrics.json` in your SuperClaude installation directory:
- Default: `~/.superclaude/.superclaude-metrics.json`
- Custom: `<install-dir>/.superclaude-metrics.json`

## Use Cases

### 1. Optimize Your Workflow

Identify your most-used commands and create aliases or shortcuts:

```bash
# See your top commands
SuperClaude metrics --summary

# If you frequently use "install --verbose --dry-run"
# Consider creating an alias in your shell config
```

### 2. Track Performance

Monitor command execution times and success rates:

```bash
# View performance trends
SuperClaude metrics --time-series day

# Identify slow operations
SuperClaude metrics --detailed
```

### 3. Debug Issues

Analyze error patterns to identify recurring problems:

```bash
# View recent errors
SuperClaude metrics --detailed

# Export error data for analysis
SuperClaude metrics --export csv --days 30
```

### 4. Generate Reports

Create beautiful reports for documentation or sharing:

```bash
# Generate monthly report
SuperClaude metrics --export html --since 2025-01-01 --until 2025-01-31

# Open in browser
open metrics_export_*.html
```

## Privacy & Security

### Data Collection Principles

1. **Minimal Collection**: Only collect what's necessary for analytics
2. **Local Storage Only**: No cloud services or external transmission
3. **User Control**: Full control over data collection and retention
4. **Transparency**: Clear documentation of what's collected and why
5. **Security**: Standard file permissions protect your data

### What's Collected

When enabled, the following data is collected:

- **Commands**: Name, flags, success/failure, duration
- **Components**: Installation, updates, usage
- **Errors**: Type, command context, timestamp
- **Sessions**: Start/end time, duration
- **NO Personal Data**: No usernames, paths, or file contents

### Anonymous Mode

When anonymous mode is enabled:
- Session IDs are randomized
- No user-specific metadata is stored
- Error details are sanitized
- Time stamps are rounded to nearest hour

### Data Retention

- **Operations**: Last 1000 operations kept
- **Sessions**: Last 100 sessions kept
- **Errors**: Last 100 errors kept
- **Automatic Cleanup**: Old data automatically removed

## Integration with SuperClaude

### Automatic Collection

When metrics are enabled, the following is automatically tracked:
- All CLI commands and their outcomes
- Component installations and updates
- Error occurrences and patterns
- Session start and end times

### Manual Integration

For custom scripts or extensions:

```python
from setup.managers.metrics_manager import MetricsManager

# Initialize
metrics = MetricsManager(install_dir)

# Record custom operation
metrics.record_command(
    command="custom_operation",
    flags=["--flag1", "--flag2"],
    success=True,
    duration=2.5,
    metadata={"custom_field": "value"}
)

# Record component usage
metrics.record_component_usage("MyComponent", "install")

# Record errors
metrics.record_error("CustomError", "operation", "Error details")
```

## Troubleshooting

### Metrics Not Recording

1. Check if metrics are enabled:
   ```bash
   SuperClaude metrics --status
   ```

2. Enable metrics if disabled:
   ```bash
   SuperClaude metrics --enable
   ```

3. Check file permissions:
   ```bash
   ls -la ~/.superclaude/.superclaude-metrics.json
   ```

### Export Issues

1. Ensure sufficient disk space
2. Check write permissions in output directory
3. Try different export format
4. Use `--verbose` flag for detailed error messages

### Performance Impact

Metrics collection has minimal performance impact:
- < 5ms overhead per command
- < 1MB storage for typical usage
- Automatic cleanup prevents unbounded growth

## Examples

### Weekly Performance Report

```bash
# Generate weekly performance report
SuperClaude metrics --export html --days 7 --output weekly_report.html

# View in browser
open weekly_report.html
```

### Component Usage Analysis

```bash
# See which components are most used
SuperClaude metrics --detailed | grep -A5 "Component Usage"

# Export for spreadsheet analysis
SuperClaude metrics --export csv
```

### Error Investigation

```bash
# View recent errors
SuperClaude metrics --detailed | grep -A10 "Recent Errors"

# Export error data for debugging
SuperClaude metrics --export json --days 1 --output errors.json
jq '.errors' errors.json
```

### Workflow Optimization

```bash
# Identify optimization opportunities
SuperClaude metrics --summary

# See time-wasting operations
SuperClaude metrics --time-series hour | grep -E "duration|slow"

# Find rarely-used flags
SuperClaude metrics --detailed | grep "flags_used"
```

## Best Practices

1. **Enable Anonymous Mode**: Protects privacy while providing useful analytics
2. **Regular Reviews**: Check metrics weekly to identify optimization opportunities
3. **Export Before Major Changes**: Create backups before system updates
4. **Clear Old Data**: Periodically clear old metrics to save space
5. **Use Time Filters**: Focus analysis on relevant time periods

## Contributing

The metrics system is designed to be extensible. To add new metrics:

1. Extend `MetricsManager` class
2. Add new data structures to schema
3. Update export formats as needed
4. Add tests for new functionality
5. Update this documentation

## Support

For issues or questions about metrics:
1. Check this documentation
2. Run `SuperClaude metrics --status` for diagnostics
3. Review logs in `~/.superclaude/logs/`
4. Open an issue on GitHub with sanitized details