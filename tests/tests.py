from django.test import TestCase
from tests.models import MyModel


class MyModelTestCase(TestCase):

    def setUp(self):
        obj1 = MyModel.objects.create(field="soft_delete")
        obj2 = MyModel.objects.create(field="hard_delete")

    def test_soft_delete_obj(self):
        obj = MyModel.objects.filter(field="soft_delete")
        obj.delete()
        obj_soft_deleted = MyModel.objects.filter(field="soft_delete")
        self.assertEqual(obj_soft_deleted.count(), 0)

    def test_soft_delete_get_obj(self):
        obj_soft_deleted = MyModel.objects_with_deleted.get(
            field="soft_delete")
        self.assertEqual(obj_soft_deleted.field, "soft_delete")

    def test_soft_restore_obj(self):
        obj_soft_deleted = MyModel.objects_with_deleted.get(
            field="soft_delete")
        obj_soft_deleted.restore()
        obj_restore_soft_deleted = MyModel.objects.filter(field="soft_delete")
        self.assertEqual(obj_soft_deleted.field, "soft_delete")

    def test_hard_delete_obj(self):
        obj = MyModel.objects_with_deleted.get(
            field="hard_delete")
        obj.delete(True)
        obj_hard_deleted = MyModel.objects.filter(field="hard_delete")
        self.assertEqual(obj_hard_deleted.count(), 0)
