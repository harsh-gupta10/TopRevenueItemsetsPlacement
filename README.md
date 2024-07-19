# An Improved Scheme for Determining Top-Revenue Itemsets for Placement in Retail Businesses

This repository contains a Python implementation of the Slot Type Utility (STU) index and TIPDS placement algorithm, as proposed in the research paper:

**Chaudhary, P., Mondal, A., & Reddy, P. K. (2020).** An improved scheme for determining top-revenue itemsets for placement in retail businesses. *International Journal of Data Science and Analytics*, 10(4), 359-375. [DOI:10.1007/s41060-020-00221-5](https://doi.org/10.1007/s41060-020-00221-5)

## Overview

The project aims to efficiently determine top-utility itemsets for retail placement considering various factors such as item price, sales frequency, and physical size (slot size). The STU index facilitates quick retrieval of high-revenue itemsets, while the TIPDS algorithm places these itemsets into premium slots to maximize revenue.


## Features

- **STU Index Structure**: Multi-level index for quick retrieval of top-utility itemsets based on slot size.
- **TIPDS Placement Algorithm**: Efficiently places itemsets into available premium slots.
- **Evaluation Metrics**: Measures execution time, index build time, number of patterns generated, total revenue, and memory usage.
- **Baseline Algorithm**: HUI-Miner for comparison of performance metrics.



## Usage

1. **Prepare the data**: Define the items with their name, price, and slot size in the code.
2. **Create the transaction database**: Populate the transaction data as a list of transactions.
3. **Set the parameters**: Adjust the following parameters in the code:
   * `lambda_val`: Number of top itemsets per level.
   * `revenue_threshold`: Minimum revenue threshold for itemsets.
   * `max_level`: Maximum index level for the STU index.
   * `num_premium_slots`: Total number of premium slots available.
4. **Run the algorithms**:
   * Call the `build_stu_index()` function to create the STU index.
   * Use the `tipds_placement()` function to perform itemset placement.
   * Evaluate the performance using the provided metrics.
5. **Compare with baseline**:
   * Implement and run the HUI-Miner algorithm on the same datasets.
   * Compare the performance metrics obtained from both algorithms.

## Evaluation Metrics



* **Execution Time (ET)**: Total time taken for index creation and item placement.
* **Index Build Time (IBT)**: Time taken specifically for building the STU index.
* **Number of Patterns Generated (NP)**: Count of candidate itemsets examined.
* **Total Revenue (TR)**: Total revenue generated by the placed itemsets.
* **Memory Usage**: Peak memory consumption during execution.
* **Scalability**: Analysis of how performance metrics scale with dataset size.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.



## Contact

For any inquiries, please contact:

* **Parul Chaudhary**: pc230@snu.edu.in
* **Anirban Mondal**: anirban.mondal@ashoka.edu.in
* **Polepalli Krishna Reddy**: pkreddy@iiit.ac.in
* **Harsh Gupta**: harsh.g@students.iiit.ac.in