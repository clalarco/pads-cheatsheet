rem @ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

set FIRST_ARG=%1
set ACTION=%FIRST_ARG%

for %%A in ("pads_maker" "pads_std_plus") do if "%FIRST_ARG%"==%%A (
	set ACTION=singlehtml
	set FIRST_ARG_IS_TOOL=1
)
if not defined FIRST_ARG_IS_TOOL shift

set PRODUCT=%1
shift
set LANGUAGE=%1
shift

if "%LANGUAGE%" == "" (
	set LANGUAGE=en
)

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR=source

set BUILDDIR=build
if NOT "%ACTION%" == "gettext" (
    set BUILDDIR=%BUILDDIR%\%LANGUAGE%
)

if "%FIRST_ARG%" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The Sphinx module was not found. Make sure you have Sphinx installed,
	echo.then set the SPHINXBUILD environment variable to point to the full
	echo.path of the 'sphinx-build' executable. Alternatively you may add the
	echo.Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %ACTION% %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% -Dlanguage=%LANGUAGE% -t%PRODUCT% %1 %2 %3 %4 %5 %6 %7 %8 %9
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %1 %2 %3 %4 %5 %6 %7 %8 %9

:end
popd
