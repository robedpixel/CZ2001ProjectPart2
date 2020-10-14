%windir%\system32\cmd.exe "/K" %systemdrive%%homepath%\Miniconda3\Scripts\activate.bat && ^
cd %~dp0 && ^
conda env create -f environment.yml && ^
conda activate CZ2002 && ^
python -m pip install snap-stanford