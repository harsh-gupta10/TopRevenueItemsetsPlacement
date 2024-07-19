from collections import defaultdict, namedtuple
import itertools

# Data structures
Item = namedtuple('Item', ['name', 'price', 'slot_size'])
Transaction = namedtuple('Transaction', ['items'])
IndexEntry = namedtuple('IndexEntry', ['itemset', 'support', 'price', 'net_revenue_per_slot'])

class STUIndex:
    def __init__(self, max_level, lambda_val):
        self.max_level = max_level
        self.lambda_val = lambda_val
        self.levels = [[] for _ in range(max_level + 1)]

def calculate_metrics(itemset, transactions, items):
    support = sum(1 for t in transactions if set(itemset).issubset(set(t.items)))
    price = sum(items[item].price for item in itemset)
    slot_size = sum(items[item].slot_size for item in itemset)
    net_revenue = support * price
    net_revenue_per_slot = net_revenue / slot_size if slot_size > 0 else 0
    return support, price, net_revenue, net_revenue_per_slot

def build_stu_index(transactions, items, max_level, lambda_val, revenue_threshold):
    stu_index = STUIndex(max_level, lambda_val)
    
    # Level 1
    level_1_items = [(item,) for item in items]
    level_1_metrics = [calculate_metrics(itemset, transactions, items) for itemset in level_1_items]
    level_1_entries = [
        IndexEntry(itemset, support, price, net_revenue_per_slot)
        for itemset, (support, price, _, net_revenue_per_slot) in zip(level_1_items, level_1_metrics)
        if net_revenue_per_slot >= revenue_threshold
    ]
    stu_index.levels[1] = sorted(level_1_entries, key=lambda x: x.net_revenue_per_slot, reverse=True)[:lambda_val]
    
    # Higher levels
    for level in range(2, max_level + 1):
        candidate_itemsets = set()
        for lower_level_itemset in stu_index.levels[level - 1]:
            for item in items:
                new_itemset = tuple(sorted(set(lower_level_itemset.itemset) | {item}))
                if len(new_itemset) == level:
                    candidate_itemsets.add(new_itemset)
        
        level_metrics = [calculate_metrics(itemset, transactions, items) for itemset in candidate_itemsets]
        level_entries = [
            IndexEntry(itemset, support, price, net_revenue_per_slot)
            for itemset, (support, price, _, net_revenue_per_slot) in zip(candidate_itemsets, level_metrics)
            if net_revenue_per_slot >= revenue_threshold
        ]
        stu_index.levels[level] = sorted(level_entries, key=lambda x: x.net_revenue_per_slot, reverse=True)[:lambda_val]
    
    return stu_index

def tipds_placement(stu_index, num_premium_slots):
    placement = []
    remaining_slots = num_premium_slots
    level = 1
    top_k = 1

    while remaining_slots > 0:
        if level > stu_index.max_level:
            level = 1
            top_k += 1

        if top_k > len(stu_index.levels[level]):
            level += 1
            continue

        itemset = stu_index.levels[level][top_k - 1].itemset
        itemset_size = sum(items[item].slot_size for item in itemset)

        if itemset_size <= remaining_slots:
            placement.append(itemset)
            remaining_slots -= itemset_size

        level += 1

    return placement

# Example usage
items = {
    'A': Item('A', 7, 3),
    'B': Item('B', 2, 2),
    'C': Item('C', 6, 1),
    'D': Item('D', 1, 2),
    'E': Item('E', 3, 4),
    'F': Item('F', 1, 3),
    'G': Item('G', 5, 2),
    'H': Item('H', 4, 5),
    'I': Item('I', 3, 2)
}

transactions = [
    Transaction(['A', 'D']),
    Transaction(['B', 'C', 'I', 'F']),
    Transaction(['A', 'C', 'G']),
    Transaction(['A', 'B', 'C', 'G', 'H']),
    Transaction(['A', 'C', 'G', 'I'])
]

max_level = 4
lambda_val = 5
revenue_threshold = 6.54
num_premium_slots = 20

stu_index = build_stu_index(transactions, items, max_level, lambda_val, revenue_threshold)
placement = tipds_placement(stu_index, num_premium_slots)

print("STU Index:")
for level, entries in enumerate(stu_index.levels):
    if entries:
        print(f"Level {level}:")
        for entry in entries:
            print(f"  {entry}")

print("\nTIPDS Placement:")
print(placement)