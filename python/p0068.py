class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified_lines = []  # Stores the final justified text lines
        current_words = []  # Words being packed into the current line
        current_words_length = 0  # Total length of words in the current line (excluding spaces)

        for word in words:
            # Check if adding the current word would exceed the maxWidth when spaces are considered
            if current_words_length + len(word) + len(current_words) > maxWidth:
                # Calculate how many spaces are needed to fill the current line
                total_spaces_needed = maxWidth - current_words_length
                # Number of gaps between words
                num_gaps = len(current_words) - 1

                if num_gaps > 0:
                    # Distribute spaces evenly among the gaps
                    spaces_per_gap = total_spaces_needed // num_gaps
                    extra_spaces = total_spaces_needed % num_gaps

                    # Build the justified line
                    justified_line = ""
                    for i in range(num_gaps):
                        # Add the word followed by spaces
                        justified_line += current_words[i] + " " * (spaces_per_gap + (1 if i < extra_spaces else 0))
                    # Add the last word without extra space after it
                    justified_line += current_words[-1]
                else:
                    # If there's only one word in the line, left-justify it
                    justified_line = current_words[0] + " " * total_spaces_needed

                justified_lines.append(justified_line)  # Store the justified line
                current_words = []  # Reset for the next line
                current_words_length = 0  # Reset the length of words for the next line

            # Add the current word to the line
            current_words.append(word)
            current_words_length += len(word)

        # Handle the last line (left-justified)
        last_line = " ".join(current_words)  # Join words with a single space
        last_line += " " * (max_width - len(last_line))  # Pad remaining spaces to the right
        justified_lines.append(last_line)

        return justified_lines