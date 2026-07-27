---
title: Docker Swarm is abandoned
date: 2026-07-27T13:30:00+02:00
lastmod: 2026-07-27T13:30:00+02:00
slug: docker-swarm
summary: "Docker Swarm is a simple alternative to Kubernetes for container orchestration, but I argue it's no longer usable for real-world workloads."
---

It's been clear for years that **Kubernetes** has won the container orchestration market, over **Docker Swarm** and **Nomad**.

Nonetheless, Docker Swarm continues to exist as a much simpler alternative and is still used and recommended by many companies for production workloads.

I argue that Swarm has been recently neglected to the point that it's **not usable anymore** for real-world workloads, and that it should be avoided.

---

Docker Swarm covers typical **production deployment needs**, such as:
- Custer management (Raft consensus, mutual TLS between nodes, node draining, etc.)
- Declarative model for services and automatic reconciliation
- Rolling updates (zero-downtime deployments) with automatic rollbacks
- Scaling
- Service discovery, built-in routing and load balancing
- Placement constraints and preferences
- Configs and secrets

Most small companies **can get very far** with this set of features. Swarm solves what plain Docker and Docker Compose don't offer, while staying away from the **complexities of Kubernetes cluster management** (especially if self-managed). While Kubernetes has many moving parts, **Docker Swarm is straightforward**: you can set up a cluster with literally two commands, without installing anything in addition to the Docker engine you already have.

It basically just works... until it doesn't. Since 2019 Docker Swarm has unfortunately received little love from its developers. It's actually not entirely clear who the developers are supposed to be. Docker Enterprise, including Swarm, was **sold to Mirantis in 2019**, which has [committed](https://www.mirantis.com/blog/mirantis-guarantees-long-term-support-for-swarm/) multiple times to keep supporting Swarm. In practice, though, features and fixes are worked on by the community and by Docker Inc. developers.

I have personally used Docker Swarm for 3 years for a couple online businesses, and while Docker Swarm has worked fine most of the time, I've had to work around **weird bugs and limitations** that make it **hard to actually recommend it** today.

The last straw is a **recent unfixed bug** that sometimes breaks connectivity between services, making Swarm basically unusable for real-world workloads.

Many people online still recommend Docker Swarm and claim that it's still usable and maintained, and that it should be preferred over Kubernetes if your workload is light (a few VMs and containers). I'm not sure how these people use Swarm in practice, but **my personal experience consisted of so many issues and limitations over the years** that I can no longer recommend Swarm and I instead suggest looking into a managed Kubernetes solution, which is often provided at no additional cost other than the underlying resources.

I'll provide a list of these issues, which at the time of writing are all unfixed except one.

## Networking

- Previous network configuration is not released after service deployment, eventually leading to broken connectivity between services ([first reported in 2025](https://github.com/moby/moby/issues/50232), [still unfixed](https://github.com/moby/moby/issues/52661)).
- The remote network IP address cannot be obtained from services ([open since 2016](https://github.com/moby/moby/issues/25526), documentation issue [open since 2015](https://github.com/moby/moby/issues/15086)).
- Node IP address reported as `0.0.0.0` when the node is a leader ([unfixed since 2017](https://github.com/moby/moby/issues/35437), requires [workaround](https://github.com/prometheus/prometheus/issues/11060) in Prometheus service discovery).

## Cluster management

- Tasks can't be rebalanced when new nodes join ([open since 2016](https://github.com/moby/moby/issues/24103)).
- Drained nodes leave tasks behind ([unfixed since 2018](https://github.com/docker/cli/issues/877)).

## CLI bugs and limitations

- Secrets cannot be updated ([first requested in 2017](https://github.com/moby/moby/issues/29882)).
- `docker service scale` with the "wait until complete" flag doesn't wait when tasks are scaled down ([open since 2017](https://github.com/docker/cli/issues/720)).
- `docker service create` never exits after `--restart-max-attempts` is reached ([open since 2022](https://github.com/moby/moby/issues/43712)).

## Stacks

Docker Swarm supports stacks, which are Compose files used to define services with a declarative approach.

- Stacks only support Compose file version 3, which was obsoleted in 2020 ([open since 2020](https://github.com/docker/cli/issues/2527)).
- The workaround to immutable secrets is secret versioning, using variable interpolation in stacks, but `docker stack deploy` doesn't allow passing variables via CLI options ([open since 2018](https://github.com/docker/cli/issues/939)) and doesn't load `.env` files ([open since 2016](https://github.com/moby/moby/issues/29133)).
- `docker stack deploy`'s exit code doesn't signal rollbacks ([open since 2026](https://github.com/docker/cli/issues/6752)), so you have to resort to asserting success with the `UpdateStatus.State` property after the deployment.
- The `UpdateStatus.State` property is missing during service creation, preventing proper deployment automation ([open since 2016](https://github.com/moby/moby/issues/28012)).
- `docker stack deploy` now has a "wait until complete" flag [after 7 years](https://github.com/docker/cli/issues/373), but the implementation is [incomplete](https://github.com/docker/cli/issues/4907) and sometimes hangs forever ([unfixed since 2024](https://github.com/docker/cli/issues/5299)).
- Variable interpolation sometimes breaks ([open since 2023](https://github.com/docker/cli/issues/4265)).
- `docker stack deploy` causes a restart of services even if their definition is unchanged ([open since 2025](https://github.com/moby/moby/issues/50167)).
- `docker stack deploy` may not pull images from private registries in certain configurations ([open since 2017](https://github.com/moby/moby/issues/31534)).

## Replicated jobs

Jobs are scheduled tasks that run once and exit.

- Replicated jobs don't respect the specified number of replicas: more than one is created even if you request one ([open since 2021](https://github.com/moby/moby/issues/42741)).
- Replicated jobs produce underflow errors and infinite retry loops ([open since 2021](https://github.com/moby/moby/issues/42742)).
- Creation of a replicated job can hang forever ([open since 2021](https://github.com/docker/cli/issues/2979)).

## Health checks

- Readiness health check waits too long ([reported in 2017](https://github.com/moby/moby/issues/33410), [PR in 2020](https://github.com/moby/moby/pull/40894), merged in 2023).
- Health check interval is calculated incorrectly if period < interval ([open since 2023](https://github.com/moby/moby/issues/46747)).

---

If you've used Docker Swarm in production, I'd be interested in hearing your opinion. Have you encountered the above issues? How did you deal with them?
