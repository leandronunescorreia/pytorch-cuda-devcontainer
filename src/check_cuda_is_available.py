import torch


def main() -> bool:
    return torch.cuda.is_available()


if __name__ == "__main__":
    print(f"cuda is available: {main()}")
