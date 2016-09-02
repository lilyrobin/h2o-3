from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

# This test is to make sure that we have fixed the following JIRA properly:
# HEXDEV-497: Merged Gzip Files not read properly.
# I will import the original files and then the gzip files and compare them to see if they are the same.

def import_folder():

  tol_time = 200              # comparing in ms or ns
  tol_numeric = 1e-5          # tolerance for comparing other numeric fields
  numElements2Compare = 0   # choose number of elements per column to compare.  Save test time.

  multi_file_gzip_comp = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/hexdev_497/milsongs_csv.zip"))
  multi_file_gzip = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/hexdev_497/milsongs_csv_gzip/000000_0.gz"))
  multi_file_gzip = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/hexdev_497/milsongs_csv_gzip/000000_0.gz"))

  multi_file_csv = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/hexdev_497/milsongs_csv"))

  # make sure orc multi-file and single big file create same H2O frame
  assert pyunit_utils.compare_frames(multi_file_csv, multi_file_gzip, numElements2Compare, tol_time, tol_numeric,
                                       True), "H2O frame parsed from multiple orc and single orc files are different!"
  assert pyunit_utils.compare_frames(multi_file_gzip, multi_file_gzip_comp, numElements2Compare, tol_time, tol_numeric,
                                       True), "H2O frame parsed from multiple orc and single orc files are different!"


if __name__ == "__main__":
  pyunit_utils.standalone_test(import_folder)
else:
  import_folder()
