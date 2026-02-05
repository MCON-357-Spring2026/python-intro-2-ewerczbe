import pytest
from exercises.src.functions import *


class TestFunctions:
    """Test suite for Exercise 1: Functions"""

    def test_calculate_area(self):
        """Test 1.1 - calculate_area function"""
        assert calculate_area(5, 3) == 15, "calculate_area(5, 3) should be 15"
        assert calculate_area(10, 10) == 100, "calculate_area(10, 10) should be 100"
        assert calculate_area(2.5, 4) == 10.0, "calculate_area(2.5, 4) should be 10.0"

    def test_format_price(self):
        """Test 1.2 - format_price function"""
        assert format_price(19.99) == "$19.99", "format_price(19.99) should be '$19.99'"
        assert format_price(19.99, "€") == "€19.99", "format_price(19.99, '€') should be '€19.99'"
        assert format_price(100, "$", 0) == "$100", "format_price(100, '$', 0) should be '$100'"

    def test_find_max(self):
        """Test 1.3 - find_max function"""
        assert find_max(1, 5, 3) == 5, "find_max(1, 5, 3) should be 5"
        assert find_max(10) == 10, "find_max(10) should be 10"
        assert find_max(-5, -2, -10) == -2, "find_max(-5, -2, -10) should be -2"

        with pytest.raises(ValueError):
            find_max()

    def test_build_tag(self):
        """Test 1.4 - build_tag function"""
        assert build_tag("div") == "<div>", "build_tag('div') should be '<div>'"
        assert build_tag("a", href="https://example.com") == '<a href="https://example.com">', "href attribute failed"

        result = build_tag("img", src="photo.jpg", alt="A photo")
        assert 'src="photo.jpg"' in result and 'alt="A photo"' in result, "Multiple attributes failed"

    def test_send_notification(self):
        """Test 1.5 - send_notification function"""
        result = send_notification("alice@example.com", "Hello!")
        assert result["to"] == "alice@example.com", "recipient failed"
        assert result["message"] == "Hello!", "message failed"
        assert result["cc"] == [], "empty cc failed"

        result2 = send_notification("bob@example.com", "Meeting", "alice@example.com", urgent=True)
        assert result2["cc"] == ["alice@example.com"], "cc list failed"
        assert result2["options"]["urgent"] == True, "options failed"

    def test_lambdas(self):
        """Test 1.6 - Lambda functions and higher-order functions"""
        assert double is not None and double(5) == 10, "double lambda failed"
        assert is_even is not None and is_even(4) == True and is_even(7) == False, "is_even lambda failed"
        assert last_char is not None and last_char("hello") == "o", "last_char lambda failed"
        assert sorted_by_length == ["c", "go", "java", "python", "javascript"], "sorted_by_length failed"
        assert positive_only == [5, 8, 10], "positive_only filter failed"
