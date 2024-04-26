if git submodule update --init --recursive; then
  cd runner_program/inference/depthai-core || exit
  if git submodule update --init --recursive; then
    cmake -S. -Bbuild || exit
    cmake --build build || exit
  fi
fi
