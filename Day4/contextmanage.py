def process(start_pt, end_pt):
    starting_pt = start_pt
    ending_pt = end_pt
    print("Starting Point: ", starting_pt)
    yield
    print("Ending Point: ", ending_pt)

with process((1,1), (2,1)):
    print("Processing...")

