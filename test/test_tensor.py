import torch


def test_torch_type():
    assert len(torch.tensor([])) == 0
