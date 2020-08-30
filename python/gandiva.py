import pandas as pd
import pyarrow as pa
import pyarrow.gandiva as gandiva
# Create a simple Pandas DataFrame
df = pd.DataFrame({"x": [1.0 * i for i in range(10)]})
table = pa.Table.from_pandas(df)
schema = pa.Schema.from_pandas(df)

builder = gandiva.TreeExprBuilder()
# Reference the column "x"
node_x = builder.make_field(table.schema.field("x"))
# Make two literals: 2.0 and 6.0
two = builder.make_literal(2.0, pa.float64())
six = builder.make_literal(6.0, pa.float64())
# Create a function for "x > 2.0"
gt_five_node = builder.make_function("greater_than",
                                     [node_x, two],
                                     pa.bool_())
# Create a function for "x < 6.0"
lt_ten_node = builder.make_function("less_than",
                                    [node_x, six],
                                    pa.bool_())
# Create an "and" node, for "(x > 2.0) and (x < 6.0)"
and_node = builder.make_and([gt_five_node, lt_ten_node])
# Make the expression a condition and create a filter
condition = builder.make_condition(and_node)
filter_ = gandiva.make_filter(table.schema, condition)