from click.testing import CliRunner

from product.model.scripts import training


def test_training():
    """Test that a minimal training runs succesfully."""
    runner = CliRunner()
    result = runner.invoke(training.run, ["--n_obs", 50])
    assert result.exit_code == 0
