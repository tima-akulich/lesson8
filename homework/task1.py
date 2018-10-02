import csv
import json
import xml.etree.ElementTree as ET


class FileConverter:
    def __init__(self, filename):
        self.filename = filename

    def read(self, format):
        return getattr(self, '_read_{}'.format(format), self._error)()

    def _read_json(self):
        file = open(self.filename, 'r')
        data = file.read()
        file.close()
        return json.loads(data)

    def _read_csv(self):
        file = open(self.filename, 'r')
        reader = csv.DictReader(file)
        for line in reader:
            yield dict(line)
        file.close()

    def _read_xml(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for item in root:
            item_root = item.getchildren()
            item_dict = {}
            for item_key in item_root:
                item_dict[item_key.tag] = item_key.text
            yield item_dict

    def _error(self):
        raise Exception('Not supported type')

    def write(self, data, format):
        method = getattr(self, '_write_{}'.format(format), self._error)
        file = open("{}.{}".format(self.filename, format), 'w')
        method(file, data)
        file.close()

    def _write_csv(self, file, data):
        writer = csv.DictWriter(file, list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)

    def _write_json(self, file, data):
        file.write(json.dumps(data))


if __name__ == '__main__':
    converter = FileConverter('test.csv')
    data = list(converter.read('csv'))
    converter.write(data, 'json')
