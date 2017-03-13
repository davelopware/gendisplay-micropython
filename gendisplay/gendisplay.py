
class GenDisplay:
    def __init__(self, width, height):
        self._width = width;
        self._height = height;
        self._buffer = []  # 0 indexed array of the rows in this virtual display. Each row should contain an array of pixels
        self._initBuffers();
        self._mappings = [];
        self._initMappings();

    def addMapping(self, genDisplayMapping):
        self._mappings.append(genDisplayMapping)

    def setPixel(self, x, y, brightness):
        self._buffer[x][y] = brightness;
        self._resync();

    def getPixel(self, x, y):
        if x < len(self._buffer) and y < len(self._buffer[x]):
            return self._buffer[x][y];
        else:
            return None;

    def clear(self):
        for idx in range(self._width):
            for idy in range(self._height):
                self._buffer[idx][idy] = 0;
        self._resync();

    def refresh(self):
        self._resync();

    def _resync(self):
        return;

    def _initBuffers(self):
        for idx in range(self._width):
            self._buffer.append([]);
            for idy in range(self._height):
                self._buffer[idx].append(0);

    def _initMappings(self):
        return;
