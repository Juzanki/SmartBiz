@echo off
echo ================================
echo 🧹 CLEANING OLD SETUP...
echo ================================

REM Delete node_modules and lock file
IF EXIST node_modules (
  echo 🗑 Deleting node_modules...
  rmdir /s /q node_modules
)
IF EXIST package-lock.json (
  echo 🗑 Deleting package-lock.json...
  del /f /q package-lock.json
)

echo.
echo ================================
echo 📦 INSTALLING DEPENDENCIES...
echo ================================

REM Install TailwindCSS, PostCSS, Autoprefixer, Forms, Typography
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest @tailwindcss/forms @tailwindcss/typography

echo.
echo ================================
echo 🚀 STARTING DEV SERVER...
echo ================================

npm run dev

pause
