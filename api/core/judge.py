class JUDGE:

    def evaluate(self, feature_spec, research):

        results = []

        for feature in feature_spec["features"]:

            name = feature["name"].lower()

            risk = "low"
            effort = "small"
            feasible = "yes"

            reasons = []

            # Authentication
            if "login" in name or "auth" in name:
                risk = "medium"
                effort = "medium"
                reasons.append(
                    "Authentication requires secure implementation"
                )

            # Dashboard
            elif "dashboard" in name:
                risk = "medium"
                effort = "medium"
                reasons.append(
                    "Dashboard requires multiple API routes"
                )

            # Upload
            elif "upload" in name:
                risk = "medium"
                effort = "medium"
                reasons.append(
                    "File handling requires validation"
                )

            # Payment
            elif "payment" in name:
                risk = "high"
                effort = "large"
                reasons.append(
                    "Payment gateway integration is complex"
                )

            results.append({
                "feature_name": feature["name"],
                "feasible": feasible,
                "risk": risk,
                "effort": effort,
                "reasons": reasons,
                "status": "evaluated"
            })

        return results