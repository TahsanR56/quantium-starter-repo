
# activate venv
source venv/Scripts/activate

pytest --headless test.py -v

# capture the exit code from pytest
EXIT_CODE=$?

# return 0 if passed, 1 if failed
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
