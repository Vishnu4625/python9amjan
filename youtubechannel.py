java={5,1200,3,88}
python={3,88,55,99,90}
print('People only subscribed to python:',python.difference(java))
print('People subscribed to both:',java.intersection(python))
print('People not subscribed to both channels:',java.symmetric_difference(python))