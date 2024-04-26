if git submodule update --init --recursive; then
  cd runner_program/inference/depthai-core || exit
  if git submodule update --init --recursive; then
    cmake -S. -Bbuild || exit
    cmake --build build || exit
  fi
fi
prompt=$(sudo -nv 2>&1)
if [ $? -eq 0 ]; then
  # exit code of sudo-command is 0
  sudo apt-get install -y libnop-dev
else echo $prompt | grep -q '^sudo:'
  echo "Script must be run with sudo rights"
fi
