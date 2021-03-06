"""
A resolution that matches an exact string. Resolutions must be paired
with questions and passed together to an actor like so:

    the_actor.should_see_the(
        (Text.of_the(LOGIN_MESSAGE), ReadsExactly("Log in below.")),
    )
"""


from hamcrest import has_string

from .base_resolution import BaseResolution


class ReadsExactly(BaseResolution):
    """
    Matches a string exactly (e.g. `"screenplay" == "screenplay"`).
    """

    expected: str
    matcher: object

    line = '"{expectation}", verbatim.'

    def __init__(self, string: str) -> None:
        self.expected = string
        self.matcher = has_string(string)
