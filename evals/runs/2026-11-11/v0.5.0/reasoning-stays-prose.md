The fix is to alert 14 days before the certificate expires rather than to add more instances. The outage started because the certificate expired at 02:00, which made the load balancer reject every new connection. The health checks use the same certificate, so they failed too. The autoscaler then decided that every instance was unhealthy and replaced them all. The new instances pulled the same expired certificate, so the loop continued until an engineer uploaded a new certificate at 02:47.

Kept as-is: "rather than to add more instances". It records the fix that the review rejected.
