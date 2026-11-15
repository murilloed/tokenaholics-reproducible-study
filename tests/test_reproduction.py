"""Guard against silently accepting changed inputs, results, or locally cached raw data."""
from pathlib import Path
import importlib.util,json,tempfile,unittest,hashlib

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reproduce',ROOT/'scripts/reproduce.py')
reproduce=importlib.util.module_from_spec(spec); spec.loader.exec_module(reproduce)

class Reproduction(unittest.TestCase):
    def test_fixed_reference_matches(self):
        self.assertEqual(reproduce.check_results(),5)

    def test_changed_input_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix='tokenaholics-check-') as folder:
            root=Path(folder); (root/'data').mkdir(); (root/'data/input.csv').write_bytes(b'changed')
            manifest=[{'path':'data/input.csv','sha256':hashlib.sha256(b'original').hexdigest()}]
            (root/'data/input_manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'checksum mismatch'):
                reproduce.check_inputs(root)

    def test_changed_numerical_result_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'Numerical result differs'):
            reproduce.compare({'mae':5.0},{'mae':5.2})

    def test_numerical_roundoff_is_allowed(self):
        reproduce.compare({'mae':5.0},{'mae':5.0+1e-10})

    def test_missing_result_fields_are_rejected(self):
        with self.assertRaisesRegex(ValueError,'keys differ'):
            reproduce.compare({'mae':5.0},{})

if __name__=='__main__': unittest.main()
