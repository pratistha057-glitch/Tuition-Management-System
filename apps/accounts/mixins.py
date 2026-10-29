from django.contrib.auth.mixins import UserPassesTestMixin


class AdminRequiredMixin(UserPassesTestMixin):
    login_url = "/accounts/login/"
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "userprofile")
            and self.request.user.userprofile.role == "ADMIN"
        )


class TeacherRequiredMixin(UserPassesTestMixin):
    login_url = "/accounts/login/"
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "userprofile")
            and self.request.user.userprofile.role == "TEACHER"
        )


class StudentRequiredMixin(UserPassesTestMixin):
    login_url = "/accounts/login/"
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "userprofile")
            and self.request.user.userprofile.role == "STUDENT"
        )


class AdminOrTeacherRequiredMixin(UserPassesTestMixin):
    login_url = "/accounts/login/"
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "userprofile")
            and self.request.user.userprofile.role in ["ADMIN", "TEACHER"]
        )
