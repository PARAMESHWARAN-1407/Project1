class RADAR:

    def research(self, feature_spec):

        title = feature_spec.get("title", "Unknown Feature")
        summary = feature_spec.get("summary", "").lower()

        patterns = []

        # -------------------------
        # Authentication
        # -------------------------
        if "login" in summary or "auth" in summary:
            patterns.append({
                "topic": "Authentication",
                "approach": "JWT Authentication",
                "notes": "Use FastAPI OAuth2 security"
            })

        # -------------------------
        # Dashboard
        # -------------------------
        if "dashboard" in summary:
            patterns.append({
                "topic": "Dashboard",
                "approach": "Role-based dashboard",
                "notes": "Separate admin and user panels"
            })

        # -------------------------
        # Upload
        # -------------------------
        if "upload" in summary or "file" in summary:
            patterns.append({
                "topic": "File Upload",
                "approach": "Multipart file upload",
                "notes": "Use UploadFile in FastAPI"
            })

        # -------------------------
        # Payment
        # -------------------------
        if "payment" in summary:
            patterns.append({
                "topic": "Payment Integration",
                "approach": "Stripe/Razorpay integration",
                "notes": "Requires secure payment gateway"
            })

        # -------------------------
        # Database
        # -------------------------
        if "database" in summary:
            patterns.append({
                "topic": "Database",
                "approach": "SQL database integration",
                "notes": "Use SQLAlchemy ORM"
            })

        # -------------------------
        # If nothing found
        # -------------------------
        if len(patterns) == 0:
            patterns.append({
                "topic": title,
                "approach": "Standard FastAPI architecture",
                "notes": "Basic modular implementation"
            })

        # -------------------------
        # LIMIT OUTPUT
        # -------------------------
        patterns = patterns[:3]

        return {
            "feature": title,
            "patterns": patterns,
            "total_patterns": len(patterns),
            "status": "researched"
        }