load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "a0fbf98d4e3a232144df4d0d80b577c7a693b570",  # 2020-04-09
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
