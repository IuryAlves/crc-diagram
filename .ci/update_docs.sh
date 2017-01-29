#!/usr/bin/env sh


cd docs

make html

mv build/html/* .

cd ..

git add .
git commit -m 'update documentation'
git push

echo "Done!"