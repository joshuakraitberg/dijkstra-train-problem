import pytest


@pytest.mark.parametrize(
    'args, output', (
        (['AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'], """Output #1: 9
Output #2: 5
Output #3: 13
Output #4: 22
Output #5: NO SUCH ROUTE
Output #6: 2
Output #7: 3
Output #8: 9
Output #9: 9
Output #10: 7
"""),
    )
)
def test_main(args, output):

    import io
    import contextlib

    from trains_problem.cli import main

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        main(args)

    assert f.getvalue() == output

