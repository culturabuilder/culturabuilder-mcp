#!/usr/bin/env python3
"""
CulturaBuilder Framework Management Hub
Unified entry point for all CulturaBuilder operations

Usage:
    CulturaBuilder install [options]
    CulturaBuilder update [options]
    CulturaBuilder uninstall [options]
    CulturaBuilder backup [options]
    CulturaBuilder --help
"""

import sys
import argparse
import subprocess
import difflib
from pathlib import Path
from typing import Dict, Callable

# Add the 'setup' directory to the Python import path (with deprecation-safe logic)

try:
    # Python 3.9+ preferred modern way
    from importlib.resources import files, as_file
    with as_file(files("setup")) as resource:
        setup_dir = str(resource)
except (ImportError, ModuleNotFoundError, AttributeError):
    # Fallback for Python < 3.9
    from pkg_resources import resource_filename
    setup_dir = resource_filename('setup', '')

# Add to sys.path
sys.path.insert(0, str(setup_dir))


# Try to import utilities from the setup package
try:
    from setup.utils.ui import (
        display_header, display_info, display_success, display_error,
        display_warning, Colors
    )
    from setup.utils.logger import setup_logging, get_logger, LogLevel
    from setup import DEFAULT_INSTALL_DIR
    from setup.managers.metrics_manager import MetricsManager
except ImportError:
    # Provide minimal fallback functions and constants if imports fail
    class Colors:
        RED = YELLOW = GREEN = CYAN = RESET = ""

    def display_error(msg): print(f"[ERROR] {msg}")
    def display_warning(msg): print(f"[WARN] {msg}")
    def display_success(msg): print(f"[OK] {msg}")
    def display_info(msg): print(f"[INFO] {msg}")
    def display_header(title, subtitle): print(f"{title} - {subtitle}")
    def get_logger(): return None
    def setup_logging(*args, **kwargs): pass
    class LogLevel:
        ERROR = 40
        INFO = 20
        DEBUG = 10


def create_global_parser() -> argparse.ArgumentParser:
    """Create shared parser for global flags used by all commands"""
    global_parser = argparse.ArgumentParser(add_help=False)

    global_parser.add_argument("--verbose", "-v", action="store_true",
                               help="Enable verbose logging")
    global_parser.add_argument("--quiet", "-q", action="store_true",
                               help="Suppress all output except errors")
    global_parser.add_argument("--install-dir", type=Path, default=DEFAULT_INSTALL_DIR,
                               help=f"Target installation directory (default: {DEFAULT_INSTALL_DIR})")
    global_parser.add_argument("--dry-run", action="store_true",
                               help="Simulate operation without making changes")
    global_parser.add_argument("--force", action="store_true",
                               help="Force execution, skipping checks")
    global_parser.add_argument("--yes", "-y", action="store_true",
                               help="Automatically answer yes to all prompts")

    return global_parser


def create_parser():
    """Create the main CLI parser and attach subcommand parsers"""
    global_parser = create_global_parser()

    parser = argparse.ArgumentParser(
        prog="CulturaBuilder",
        description="CulturaBuilder Framework Management Hub - Unified CLI",
        epilog="""
Examples:
  CulturaBuilder install --dry-run
  CulturaBuilder update --verbose
  CulturaBuilder backup --create
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[global_parser]
    )

    parser.add_argument("--version", action="version", version="CulturaBuilder v3.0.0")

    subparsers = parser.add_subparsers(
        dest="operation",
        title="Operations",
        description="Framework operations to perform"
    )

    return parser, subparsers, global_parser


def setup_global_environment(args: argparse.Namespace):
    """Set up logging and shared runtime environment based on args"""
    # Determine log level
    if args.quiet:
        level = LogLevel.ERROR
    elif args.verbose:
        level = LogLevel.DEBUG
    else:
        level = LogLevel.INFO

    # Define log directory unless it's a dry run
    log_dir = args.install_dir / "logs" if not args.dry_run else None
    setup_logging("culturabuilder_hub", log_dir=log_dir, console_level=level)

    # Log startup context
    logger = get_logger()
    if logger:
        logger.debug(f"CulturaBuilder called with operation: {getattr(args, 'operation', 'None')}")
        logger.debug(f"Arguments: {vars(args)}")


def get_operation_modules() -> Dict[str, str]:
    """Return supported operations and their descriptions"""
    return {
        "install": "Install CulturaBuilder framework components",
        "update": "Update existing CulturaBuilder installation",
        "uninstall": "Remove CulturaBuilder installation",
        "backup": "Backup and restore operations"
    }


def load_operation_module(name: str):
    """Try to dynamically import an operation module"""
    try:
        return __import__(f"setup.operations.{name}", fromlist=[name])
    except ImportError as e:
        logger = get_logger()
        if logger:
            logger.error(f"Module '{name}' failed to load: {e}")
        return None


def register_operation_parsers(subparsers, global_parser) -> Dict[str, Callable]:
    """Register subcommand parsers and map operation names to their run functions"""
    operations = {}
    for name, desc in get_operation_modules().items():
        module = load_operation_module(name)
        if module and hasattr(module, 'register_parser') and hasattr(module, 'run'):
            module.register_parser(subparsers, global_parser)
            operations[name] = module.run
        else:
            # If module doesn't exist, register a stub parser and fallback to legacy
            parser = subparsers.add_parser(name, help=f"{desc} (legacy fallback)", parents=[global_parser])
            parser.add_argument("--legacy", action="store_true", help="Use legacy script")
            operations[name] = None
    return operations


def handle_legacy_fallback(op: str, args: argparse.Namespace) -> int:
    """Run a legacy operation script if module is unavailable"""
    script_path = Path(__file__).parent / f"{op}.py"

    if not script_path.exists():
        display_error(f"No module or legacy script found for operation '{op}'")
        return 1

    display_warning(f"Falling back to legacy script for '{op}'...")

    cmd = [sys.executable, str(script_path)]

    # Convert args into CLI flags
    for k, v in vars(args).items():
        if k in ['operation', 'install_dir'] or v in [None, False]:
            continue
        flag = f"--{k.replace('_', '-')}"
        if v is True:
            cmd.append(flag)
        else:
            cmd.extend([flag, str(v)])

    try:
        return subprocess.call(cmd)
    except Exception as e:
        display_error(f"Legacy execution failed: {e}")
        return 1


def main() -> int:
    """Main entry point"""
    start_time = None
    metrics_manager = None
    operation = None
    
    try:
        import time
        start_time = time.time()
        
        parser, subparsers, global_parser = create_parser()
        operations = register_operation_parsers(subparsers, global_parser)
        args = parser.parse_args()

        # No operation provided? Show help manually unless in quiet mode
        if not args.operation:
            if not args.quiet:
                display_header("CulturaBuilder Framework v3.0", "Unified CLI for all operations")
                print(f"{Colors.CYAN}Available operations:{Colors.RESET}")
                for op, desc in get_operation_modules().items():
                    print(f"  {op:<12} {desc}")
            return 0

        # Handle unknown operations and suggest corrections
        if args.operation not in operations:
            close = difflib.get_close_matches(args.operation, operations.keys(), n=1)
            suggestion = f"Did you mean: {close[0]}?" if close else ""
            display_error(f"Unknown operation: '{args.operation}'. {suggestion}")
            return 1

        # Setup global context (logging, install path, etc.)
        setup_global_environment(args)
        logger = get_logger()
        
        # Initialize metrics manager if available
        try:
            metrics_manager = MetricsManager(args.install_dir)
            operation = args.operation
            # Extract flags from args
            flags = []
            for key, value in vars(args).items():
                if key not in ['operation', 'install_dir'] and value:
                    if value is True:
                        flags.append(f"--{key.replace('_', '-')}")
                    else:
                        flags.append(f"--{key.replace('_', '-')}={value}")
        except Exception as e:
            # Metrics collection is optional, continue without it
            if logger:
                logger.debug(f"Metrics manager not available: {e}")

        # Execute operation
        run_func = operations.get(args.operation)
        if run_func:
            if logger:
                logger.info(f"Executing operation: {args.operation}")
            result = run_func(args)
            
            # Record successful operation
            if metrics_manager and start_time:
                duration = time.time() - start_time
                metrics_manager.record_command(
                    command=operation,
                    flags=flags if 'flags' in locals() else [],
                    success=(result == 0),
                    duration=duration
                )
            
            return result
        else:
            # Fallback to legacy script
            if logger:
                logger.warning(f"Module for '{args.operation}' missing, using legacy fallback")
            result = handle_legacy_fallback(args.operation, args)
            
            # Record legacy operation
            if metrics_manager and start_time:
                duration = time.time() - start_time
                metrics_manager.record_command(
                    command=operation,
                    flags=flags if 'flags' in locals() else [],
                    success=(result == 0),
                    duration=duration,
                    metadata={"legacy": True}
                )
            
            return result

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Operation cancelled by user{Colors.RESET}")
        # Record session end if metrics are enabled
        if metrics_manager:
            metrics_manager.record_session_end()
        return 130
    except Exception as e:
        try:
            logger = get_logger()
            if logger:
                logger.exception(f"Unhandled error: {e}")
            # Record error if metrics are available
            if metrics_manager and operation:
                metrics_manager.record_error(
                    error_type=type(e).__name__,
                    command=operation,
                    details=str(e)
                )
        except:
            print(f"{Colors.RED}[ERROR] {e}{Colors.RESET}")
        return 1
    finally:
        # Always try to record session end
        if metrics_manager:
            try:
                metrics_manager.record_session_end()
            except:
                pass


# Entrypoint guard
if __name__ == "__main__":
    sys.exit(main())
    


# CulturaBuilder
