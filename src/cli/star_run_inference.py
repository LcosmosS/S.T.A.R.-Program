import argparse
import yaml
from src.pipeline.full_inference import run_full_inference

def main():
    parser = argparse.ArgumentParser(description="Run S.T.A.R. cosmology inference")
    parser.add_argument("config", help="Path to YAML config file")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    run_full_inference(config)

if __name__ == "__main__":
    main()
