import yaml
import os
from perf_tool import PerfTool
from perf_data_processor import PerfDataProcessor

def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed configuration.
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    # Load configuration
    config_path = "./config.yaml"
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    config = load_config(config_path)

    output_dir = config.get("output_dir", "./data")
    os.makedirs(output_dir, exist_ok=True)

    # Initialize PerfTool
    perf_tool = PerfTool(output_dir=output_dir)
    events = config.get("events", ["cycles", "instructions", "branch-misses"])
    frequency = config.get("frequency", 999)
    duration = config.get("duration", 10)

    # Step 1: Record performance data
    print("Recording performance data...")
    perf_tool.record(events=events, frequency=frequency, duration=duration)

    # Step 2: Generate perf script
    print("Generating perf script...")
    perf_tool.script()

    # Step 3: Process and analyze data
    print("Processing and analyzing data...")
    processor = PerfDataProcessor()
    script_path = os.path.join(output_dir, "perf.script")
    parsed_data = processor.parse_perf_script(script_path)

    print("Parsed Data:")
    print(parsed_data.head())

    event_summary = processor.summarize_events(parsed_data)
    print("Event Summary:")
    print(event_summary)

if __name__ == "__main__":
    main()