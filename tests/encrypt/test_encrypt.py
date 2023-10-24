from challenges.challenge_encrypt_message import encrypt_message
import pytest

message = ":butterfly::unicorn::bee::duck::bee::unicorn:"


def test_encrypt_message():
    # Test for valid inputs
    assert (
        encrypt_message(message, 1)
        == ":_:nrocinu::eeb::kcud::eeb::nrocinu::ylfrettub"
    )
    assert (
        encrypt_message(message, 2)
        == ":nrocinu::eeb::kcud::eeb::nrocinu::ylfrettu_b:"
    )

    # Test for invalid 'key' input
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, "1")

    # Test for invalid 'message' input
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1234, 1)

    # Test for invalid 'key' out of range
    assert (
        encrypt_message(message, 100)
        == ":nrocinu::eeb::kcud::eeb::nrocinu::ylfrettub:"
    )

    # Test for edge case: empy message
    assert encrypt_message("", 2) == ""
