#!/usr/bin/env bash

set -e

TARGET_BRANCH="gh-pages"
REPO=`git config remote.origin.url`
SSH_REPO=${REPO/https:\/\/github.com\//git@github.com:}
SHA="$(git rev-parse --verify HEAD)"
ENCRYPTED_KEY_VAR="encrypted_${ENCRYPTION_LABEL}_key"
ENCRYPTED_IV_VAR="encrypted_${ENCRYPTION_LABEL}_iv"
ENCRYPTED_KEY=${!ENCRYPTED_KEY_VAR}
ENCRYPTED_IV=${!ENCRYPTED_IV_VAR}

function build_docs() {
    cd docs
    make html
    cp -R build/html/* ..
}

function add_encrypted_key(){
    openssl aes-256-cbc -K $ENCRYPTED_KEY -iv $ENCRYPTED_IV -in key.enc -out key -d
    chmod 600 key
    eval `ssh-agent -s`
    ssh-add key
}


if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_BRANCH" != "master" ]; then
    echo "Skipping build docs"
    exit 0
fi

git config --global user.name "Iury Souza"
git config --global user.email "$COMMIT_AUTHOR_EMAIL"
git clone $REPO repo


cd repo
git checkout $TARGET_BRANCH || git checkout --orphan $TARGET_BRANCH
git merge -s recursive -X theirs -m 'merging master' master
echo
build_docs

cd ..

set +e
find . -not -name "*.html" \
       -not -name "*.js" \
       -not -name "*.css" \
       -not -path "*/_static*" \
       -not -path "*/_images*" \
       -not -path "*/\.git*" \
       -not -name ".nojekyll" \
       -not -name "key.enc" -exec rm -rf "{}" \;

set -e
add_encrypted_key

git add --all .
git commit -m 'update documentation for commit: $SHA'
git push $SSH_REPO HEAD:$TARGET_BRANCH

echo "Done!"
