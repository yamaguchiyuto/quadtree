echo ===== Input data =====
cat sample_data

echo
echo ===== Command =====
echo python main.py --infile sample_data --upper 0 0 --lower 1 1 --maxdepth 3 --maxpoints 3

echo
echo ===== Output =====
python main.py --infile sample_data --upper 0 0 --lower 1 1 --maxdepth 3 --maxpoints 3
