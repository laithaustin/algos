import pytest
from gravity_flip import gravity_flip


class TestGravityFlip:
    """Test cases for the gravity flip problem."""

    def test_example_1(self):
        """
        Example 1 from problem description.
        Initial: [3, 2, 1, 2]
        After gravity flip, cubes redistribute to the right.
        """
        assert gravity_flip(4, [3, 2, 1, 2]) == [1, 2, 2, 3]

    def test_example_2(self):
        """
        Example 2 from problem description.
        Initial: [3, 8]
        Gravity switch doesn't change heights (already sorted).
        """
        assert gravity_flip(2, [3, 8]) == [3, 8]

    def test_single_column(self):
        """Test with a single column."""
        assert gravity_flip(1, [5]) == [5]

    def test_already_sorted(self):
        """Test with columns already sorted in ascending order."""
        assert gravity_flip(5, [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test with columns sorted in descending order."""
        assert gravity_flip(5, [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_all_same_height(self):
        """Test with all columns having the same height."""
        assert gravity_flip(4, [3, 3, 3, 3]) == [3, 3, 3, 3]

    def test_two_columns_unsorted(self):
        """Test with two columns that need to be swapped."""
        assert gravity_flip(2, [5, 2]) == [2, 5]

    def test_large_values(self):
        """Test with larger column heights (up to 100)."""
        assert gravity_flip(3, [100, 1, 50]) == [1, 50, 100]

    def test_random_distribution(self):
        """Test with a random distribution of cubes."""
        assert gravity_flip(6, [4, 7, 2, 9, 1, 3]) == [1, 2, 3, 4, 7, 9]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
