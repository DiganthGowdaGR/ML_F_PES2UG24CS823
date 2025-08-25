import torch
import math

def get_entropy_of_dataset(tensor: torch.Tensor):
    """
    Calculate the entropy of the entire dataset.
    """
    target_col = tensor[:, -1]
    unique_classes, counts = torch.unique(target_col, return_counts=True)
    total = counts.sum().item()
    probs = counts.float() / total
    entropy = -torch.sum(probs * torch.log2(probs))
    return entropy.item()


def get_avg_info_of_attribute(tensor: torch.Tensor, attribute: int):
    """
    Calculate the weighted average information (entropy) for a given attribute.
    """
    target_idx = -1
    total_samples = tensor.shape[0]
    unique_values, counts = torch.unique(tensor[:, attribute], return_counts=True)
    avg_info = 0.0

    for val, count in zip(unique_values, counts):
        subset = tensor[tensor[:, attribute] == val]
        subset_size = subset.shape[0]
        subset_target = subset[:, target_idx]
        unique_classes, subset_counts = torch.unique(subset_target, return_counts=True)

        probs = subset_counts.float() / subset_size
        entropy = -torch.sum(probs * torch.log2(probs))
        avg_info += (subset_size / total_samples) * entropy

    return avg_info.item()


def get_information_gain(tensor: torch.Tensor, attribute: int):
    """
    Calculate information gain for a given attribute.
    """
    entropy_dataset = get_entropy_of_dataset(tensor)
    avg_info = get_avg_info_of_attribute(tensor, attribute)
    info_gain = entropy_dataset - avg_info
    return round(info_gain, 4)


def get_selected_attribute(tensor: torch.Tensor):
    """
    Select the attribute with the highest information gain.
    Returns: (dict of attribute:index -> information gain, best attribute index)
    """
    num_features = tensor.shape[1] - 1  # Exclude target column
    info_gains = {}

    for attr in range(num_features):
        gain = get_information_gain(tensor, attr)
        info_gains[attr] = gain

    best_attribute = max(info_gains, key=info_gains.get)
    return info_gains, best_attribute
