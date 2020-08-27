#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pypette import BashJob, Job, Pipe


def wish():
    print("Hello World!")


wish_job = Job(wish)

build_job = BashJob(["python", "setup.py", "build"])

test_job = BashJob(["python", "setup.py", "test"])

clean_job = BashJob(["rm", "*.pyc"])


def goodbye(msg):
    print("Goodbye {}!".format(msg))


goodbye_job = Job(goodbye, args=("World",))

# Pipeline can be created using add_jobs
p = Pipe("Pipeline")
p.add_jobs([wish_job])
p.add_jobs([build_job, test_job], run_in_parallel=True)
p.add_jobs([clean_job])
p.add_jobs([goodbye_job])

# Or using add_stage
p = Pipe("Pipeline")
p.add_stage(wish_job)
p.add_stage(build_job, test_job)
p.add_stage(clean_job)
p.add_stage(goodbye_job)

# Can check how the pipeline looks like
p.graph()

# Can run the pipeline using
p.run()

# Can check on the success states of different stages of pipeline using
p.report()

__all__ = [n for n in globals() if n[:1] != '_']
