import camelot


tables = camelot.read_pdf('data/foo.pdf', pages='1')
print(tables)

tables.export('data/foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')
print(tables[0].df)