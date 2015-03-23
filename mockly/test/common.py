from datetime import datetime

class MockDateTime(datetime):
    NOW = datetime.utcnow()
    @staticmethod
    def utcnow():
        return MockDateTime.NOW

    @staticmethod
    def strptime(val, fmt): # pylint: disable=unused-argument
        return MockDateTime.NOW

    @staticmethod
    def utcfromtimestamp(timestamp): # pylint: disable=unused-argument
        return MockDateTime.NOW