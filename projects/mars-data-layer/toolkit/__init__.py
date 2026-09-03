"""MARS DB Toolkit — closed parameterized operations for app_iseo_sales.

No generic execute_sql product surface. Call named ops that wrap SECURITY DEFINER
functions only.
"""

from .ops_iseo_sales import IseoSalesOps, ALLOWED_OPS

__all__ = ["IseoSalesOps", "ALLOWED_OPS"]
