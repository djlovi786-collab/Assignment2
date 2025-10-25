"""Entry point for the refactored text statistics program."""

from typing import List

from package.io_ops import (
    DEFAULT_INPUT_FILENAME,
    DEFAULT_OUTPUT_FILENAME,
    display_results,
    get_input_text,
    save_output_lines,
)
from package.text_stats import (
    avg_wrd_lenght,
    character_count,
    freq_cmn_wrds,
    word_extraction,
    wrd_unq_wrd_cnt,
)


def build_result_lines(text_content: str) -> List[str]:
    """Compute the six required output lines for the report."""

    characters_with_spaces, characters_no_spaces = character_count(text_content)
    words = word_extraction(text_content)
    word_count, unique_word_count = wrd_unq_wrd_cnt(words)
    average_word_length = avg_wrd_lenght(words, word_count)
    most_common_line = freq_cmn_wrds(words, word_count)

    return [
        f"Word count: {word_count}",
        f"Unique words: {unique_word_count}",
        f"Characters (with spaces): {characters_with_spaces}",
        f"Characters (no spaces): {characters_no_spaces}",
        f"Average word length: {average_word_length}",
        most_common_line,
    ]


def main() -> None:
    _, text_content = get_input_text(DEFAULT_INPUT_FILENAME)
    result_lines = build_result_lines(text_content)

    display_results(result_lines)
    save_output_lines(result_lines, DEFAULT_OUTPUT_FILENAME)


if __name__ == "__main__":
    main()