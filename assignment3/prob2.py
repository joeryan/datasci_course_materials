import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document order_id
    # value: remaining fields
    key = record[1]
    # rec_type = record[0]
    remaining_rec = record[2:]
    mr.emit_intermediate(key, remaining_rec)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of list of fields
    total_rec = []
    for v in list_of_values:
        for field in v:
          total_rec.append(v)
    mr.emit((key, total_rec))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
