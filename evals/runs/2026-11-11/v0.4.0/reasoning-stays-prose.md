The fix is to alert 14 days before the certificate expires. More instances do not fix the problem, because each new instance pulls the same certificate.

The outage started because the certificate expired at 02:00, which made the load balancer reject every new connection. The health checks use the same certificate, so they failed too. The autoscaler then decided that every instance was unhealthy and replaced them all. The new instances pulled the same expired certificate, so the loop continued until an engineer uploaded a new certificate at 02:47.

Kept as-is: "More instances do not fix the problem". The source rejects that fix by name, and a reader of an outage review is likely to propose it.
Reader: an engineer who reads the incident review and decides which fix to approve.
