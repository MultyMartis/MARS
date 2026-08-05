# TEST-LEAD-SUPPRESSION-v1

For `is_probable_test=true`:

- preserve all semantic fields and name (including `test`)
- show `🧪 Тестовая заявка`
- `first_reply_ready=false`
- `first_reply_mode=test_suppressed`
- `first_reply_omitted_reason=probable_test`
- card: `Черновик ответа не сформирован: тестовая заявка.`
- no copy `<pre>` block
- do not auto-classify as spam
- exclude from production sales stats when exclusion already configured

Harness H12/H12b/H34 PASS. Live case H: mode=`test_suppressed`.
