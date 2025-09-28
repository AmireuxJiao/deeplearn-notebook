def require_role(role):
    def decorator(func):
        def wapper(*arge, **kwargs):
            user_role = kwargs.get("role", "guest")
            if user_role != role:
                print(f"Access denied! Need role: {role}")
                return
            print(f"Access granted for role: {role}")
            return func(*arge, **kwargs)
        return wapper
    return decorator

@require_role("admin")
def delete_user(user_id, role="guest"):
    print(f"Deleting user {user_id}")
    return

delete_user(47)
delete_user(47, role="admin")