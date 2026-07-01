class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters on the left
            if not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters on the right
            elif not s[right].isalnum():
                right -= 1

            # Both characters are valid
            else:
                # Compare ignoring case
                if s[left].lower() != s[right].lower():
                    return False

                # Move both pointers inward
                left += 1
                right -= 1

        # No mismatches found
        return True