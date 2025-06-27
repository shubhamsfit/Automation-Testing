import pytest

@pytest.fixture(autouse=True)
def print_test_name(request):
    print(f"\nRunning: {request.node.name}")
