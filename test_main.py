"""Automated tests for the RuleBot command-line chatbot."""

import unittest
from datetime import datetime
from unittest.mock import patch

import main


class FixedDateTime(datetime):
    @classmethod
    def now(cls, tz=None) -> "FixedDateTime":
        return cls(2026, 10, 25, 19, 23, 10)


class NormalizeInputTests(unittest.TestCase):
    def test_normalizes_case_spaces_and_punctuation(self) -> None:
        self.assertEqual(main.normalize_input("  GOOD morning!!! "), "good morning")


class GenerateResponseTests(unittest.TestCase):
    def test_recognized_greeting(self) -> None:
        self.assertEqual(main.generate_response("hello"), main.RESPONSES["hello"])

    def test_greeting_with_different_capitalization(self) -> None:
        self.assertEqual(main.generate_response("HELLO"), main.RESPONSES["hello"])

    def test_greeting_with_extra_spaces(self) -> None:
        self.assertEqual(main.generate_response("  hi   "), main.RESPONSES["hi"])

    def test_recognized_question(self) -> None:
        self.assertEqual(
            main.generate_response("What is Python?"),
            main.RESPONSES["what is python"],
        )

    def test_date_query_uses_current_date_format(self) -> None:
        with patch.object(main, "datetime", FixedDateTime):
            response = main.generate_response("what is the date")

        self.assertEqual(response, "Today's date is Sunday, October 25, 2026.")

    def test_time_query_uses_current_time_format(self) -> None:
        with patch.object(main, "datetime", FixedDateTime):
            response = main.generate_response("what time is it")

        self.assertEqual(response, "The current time is 07:23:10 PM.")

    def test_unknown_input_uses_fallback(self) -> None:
        self.assertIn(
            "I'm not sure how to respond",
            main.generate_response("Can you recommend a restaurant?"),
        )

    def test_empty_input_gets_a_prompt(self) -> None:
        self.assertIn("didn't receive a message", main.generate_response("   "))

    def test_exit_command_gets_goodbye(self) -> None:
        self.assertIn("Goodbye", main.generate_response("bye"))

    def test_punctuation_is_ignored_for_matching(self) -> None:
        self.assertEqual(
            main.generate_response("GOOD morning!!!"),
            main.RESPONSES["good morning"],
        )

    def test_phrase_matching_does_not_match_inside_a_word(self) -> None:
        self.assertIn(
            "I'm not sure how to respond",
            main.generate_response("this is a new question"),
        )


class ChatTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["hello", "quit"])
    @patch("builtins.print")
    def test_chat_continues_until_exit_command(
        self, mocked_print: unittest.mock.MagicMock, _mocked_input: unittest.mock.MagicMock
    ) -> None:
        main.chat()

        printed_lines = [call.args[0] for call in mocked_print.call_args_list]
        self.assertTrue(any("Welcome to RuleBot" in line for line in printed_lines))
        self.assertTrue(any("Hello! Nice to meet you." in line for line in printed_lines))
        self.assertTrue(any("Goodbye" in line for line in printed_lines))

    @patch("builtins.input", side_effect=EOFError)
    @patch("builtins.print")
    def test_end_of_input_exits_cleanly(
        self, mocked_print: unittest.mock.MagicMock, _mocked_input: unittest.mock.MagicMock
    ) -> None:
        main.chat()

        self.assertTrue(
            any("Goodbye" in call.args[0] for call in mocked_print.call_args_list)
        )


if __name__ == "__main__":
    unittest.main()
