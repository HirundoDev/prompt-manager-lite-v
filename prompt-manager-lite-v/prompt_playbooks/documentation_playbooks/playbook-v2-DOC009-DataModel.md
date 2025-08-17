# Playbook: DOC009-DataModel.md

## Document Purpose
Create comprehensive data model documentation following 2025 best practices, focusing on domain-driven design, privacy compliance, performance optimization, and modern data governance for scalable applications.

## 2025 Best Practices Integration

### Modern Data Modeling Approaches
- **Domain-Driven Design (DDD)** with bounded contexts and aggregates
- **Privacy by Design** with GDPR/CCPA compliance built into data structure
- **Performance First** optimization for read/write patterns and query performance
- **Data Governance** with comprehensive quality monitoring and lineage tracking

### Advanced Database Features
- **JSONB for Flexibility** with GIN indexes for efficient querying
- **Row-Level Security** for fine-grained access control
- **Partitioning Strategies** for large-scale data management
- **Materialized Views** for performance optimization

### Data Security & Compliance
- **Column-Level Encryption** for sensitive personal data
- **Audit Trails** with comprehensive change tracking
- **Data Classification** with sensitivity levels and access controls
- **Automated Retention** policies with archival strategies

## Document Structure

### 1. Data Model Overview
- Executive summary with modern data architecture principles
- Data model philosophy emphasizing DDD and privacy by design
- Key metrics and goals for performance and quality
- Database technology stack with modern tools

### 2. Architecture & Design Principles
- Database design patterns following 2025 standards
- Domain-driven design implementation
- Performance optimization strategies
- Data governance framework with classification and retention

### 3. Entity Relationship Diagram
- High-level ERD with comprehensive entity relationships
- Domain-specific ERDs for bounded contexts
- Visual representation using Mermaid diagrams
- Clear relationship cardinalities and constraints

### 4. Entity Definitions
- Complete entity definitions with SQL DDL
- Business rules and constraints documentation
- Index strategies for performance optimization
- Data validation and integrity rules

### 5. Relationships & Constraints
- Primary relationships with referential integrity
- Foreign key constraints with cascade rules
- Check constraints for data validation
- Unique constraints and business rules

### 6. Data Security & Privacy
- Data classification by sensitivity levels
- Personal data inventory for GDPR compliance
- Column-level encryption for sensitive data
- Row-level security policies and access control

### 7. Performance & Indexing
- Comprehensive indexing strategy
- Query optimization techniques
- Materialized views for reporting
- Partitioning strategies for scalability

### 8. Data Lifecycle Management
- Entity state transitions and workflows
- Automated data management with triggers
- Data archival and retention policies
- Soft delete and recovery procedures

### 9. Views & Materialized Views
- Reporting views for business intelligence
- Materialized views for performance
- API data views for external consumption
- Analytics and dashboard views

### 10. Data Validation & Quality
- Data quality rules and validation functions
- Automated quality monitoring
- Quality metrics dashboard
- Data integrity checks and alerts

### 11. Analytics & Reporting
- Business intelligence views
- Time series analytics
- Executive dashboard metrics
- Data export and integration views

### 12. Migration & Versioning
- Schema versioning strategy
- Migration framework and procedures
- Backward compatibility maintenance
- Rollback procedures and validation

### 13. Data Dictionary
- Complete entity reference with privacy levels
- Enumeration types and constraints
- Column descriptions and business rules
- Data lineage and relationships

## Key Implementation Guidelines

### Domain-Driven Design Implementation
```sql
-- Aggregate root with bounded context
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile JSONB DEFAULT '{}',
    status user_status DEFAULT 'active',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Value object as JSONB
ALTER TABLE users ADD COLUMN address JSONB;
ALTER TABLE users ADD CONSTRAINT chk_address_format 
    CHECK (
        address IS NULL OR (
            address ? 'street' AND 
            address ? 'city' AND 
            address ? 'country'
        )
    );
```

### Privacy by Design Implementation
```sql
-- Personal data classification
CREATE TABLE personal_data_inventory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_name VARCHAR(100) NOT NULL,
    column_name VARCHAR(100) NOT NULL,
    data_category personal_data_category NOT NULL,
    processing_purpose TEXT NOT NULL,
    retention_period INTERVAL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Data subject rights implementation
CREATE TABLE data_subject_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    request_type data_request_type NOT NULL,
    status request_status DEFAULT 'pending',
    requested_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    completed_at TIMESTAMP WITH TIME ZONE
);
```

### Performance Optimization
```sql
-- Composite indexes for common queries
CREATE INDEX idx_tasks_project_status ON tasks(project_id, status);
CREATE INDEX idx_tasks_assignee_due_date ON tasks(assigned_to, due_date);

-- Partial indexes for filtered queries
CREATE INDEX idx_active_users ON users(id) WHERE status = 'active';
CREATE INDEX idx_pending_tasks ON tasks(id) WHERE status IN ('todo', 'in_progress');

-- JSONB indexes for flexible queries
CREATE INDEX idx_users_profile_gin ON users USING GIN(profile);
CREATE INDEX idx_users_profile_skills ON users USING GIN((profile->'skills'));
```

### Data Security Implementation
```sql
-- Row-level security
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

CREATE POLICY project_access_policy ON projects
    FOR ALL TO application_role
    USING (
        organization_id IN (
            SELECT organization_id 
            FROM user_organizations 
            WHERE user_id = current_setting('app.current_user_id')::UUID
            AND active = TRUE
        )
    );

-- Column-level encryption
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE OR REPLACE FUNCTION encrypt_personal_data(data TEXT, key TEXT)
RETURNS BYTEA AS $$
BEGIN
    RETURN pgp_sym_encrypt(data, key);
END;
$$ LANGUAGE plpgsql;
```

## Data Quality and Governance

### Quality Monitoring
```sql
-- Data quality checks
CREATE TABLE data_quality_checks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    check_name VARCHAR(255) NOT NULL,
    table_name VARCHAR(100) NOT NULL,
    check_type quality_check_type NOT NULL,
    check_query TEXT NOT NULL,
    threshold_value NUMERIC,
    status check_status DEFAULT 'pending'
);

-- Automated quality validation
CREATE OR REPLACE FUNCTION run_data_quality_checks()
RETURNS void AS $$
DECLARE
    check_record RECORD;
    result_count NUMERIC;
BEGIN
    FOR check_record IN 
        SELECT * FROM data_quality_checks WHERE status != 'disabled'
    LOOP
        EXECUTE check_record.check_query INTO result_count;
        
        UPDATE data_quality_checks 
        SET 
            last_run = NOW(),
            last_result = result_count,
            status = CASE 
                WHEN result_count <= COALESCE(threshold_value, 0) THEN 'passed'
                ELSE 'failed'
            END
        WHERE id = check_record.id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
```

### Audit Trail Implementation
```sql
-- Comprehensive audit logging
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    entity_type VARCHAR(100) NOT NULL,
    entity_id UUID NOT NULL,
    action audit_action NOT NULL,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Automatic audit trigger
CREATE OR REPLACE FUNCTION audit_trigger_function()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_logs (
        user_id,
        entity_type,
        entity_id,
        action,
        old_values,
        new_values
    ) VALUES (
        COALESCE(current_setting('app.current_user_id', true)::UUID, NULL),
        TG_TABLE_NAME,
        COALESCE(NEW.id, OLD.id),
        TG_OP,
        CASE WHEN TG_OP = 'DELETE' THEN row_to_json(OLD) ELSE NULL END,
        CASE WHEN TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN row_to_json(NEW) ELSE NULL END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;
```

## Migration and Versioning

### Schema Evolution Strategy
```sql
-- Schema version tracking
CREATE TABLE schema_migrations (
    version VARCHAR(50) PRIMARY KEY,
    description TEXT NOT NULL,
    applied_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    applied_by VARCHAR(100) DEFAULT current_user,
    checksum VARCHAR(64)
);

-- Migration validation
CREATE OR REPLACE FUNCTION validate_migration(migration_version VARCHAR(50))
RETURNS BOOLEAN AS $$
DECLARE
    row_count_before INTEGER;
    row_count_after INTEGER;
BEGIN
    -- Pre-migration validation
    SELECT COUNT(*) INTO row_count_before FROM users;
    
    -- Post-migration validation
    SELECT COUNT(*) INTO row_count_after FROM users;
    
    IF row_count_before != row_count_after THEN
        RAISE EXCEPTION 'Migration validation failed: row count mismatch';
    END IF;
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
```

### Backward Compatibility
```sql
-- Maintain compatibility with views
CREATE VIEW users_legacy AS
SELECT 
    id,
    email,
    first_name || ' ' || last_name as full_name,
    status,
    created_at,
    updated_at
FROM users;

-- Gradual deprecation process
COMMENT ON COLUMN users.full_name_deprecated IS 
'DEPRECATED: Use first_name and last_name separately. Will be removed in v2.0';
```

## Customization Guidelines

### Project-Specific Adaptations
1. **Domain Modeling:** Adapt entities based on business domain and requirements
2. **Privacy Requirements:** Customize data classification based on regulatory needs
3. **Performance Needs:** Adjust indexing and partitioning based on query patterns
4. **Scalability Requirements:** Design partitioning strategy for expected data volume
5. **Integration Needs:** Create appropriate views and APIs for external systems

### Industry-Specific Considerations
- **E-commerce:** Product catalogs, inventory management, order processing
- **Healthcare:** Patient data, medical records, HIPAA compliance
- **Financial Services:** Transaction data, regulatory reporting, PCI compliance
- **SaaS Applications:** Multi-tenancy, subscription management, usage tracking

## Advanced Features

### Modern Database Capabilities
```sql
-- Generated columns for computed values
ALTER TABLE users ADD COLUMN full_name_generated TEXT 
    GENERATED ALWAYS AS (first_name || ' ' || last_name) STORED;

-- JSON path indexes for specific queries
CREATE INDEX idx_user_skills ON users USING GIN ((profile->'skills'));

-- Exclusion constraints for business rules
ALTER TABLE user_organizations ADD CONSTRAINT exclude_duplicate_owner
    EXCLUDE (organization_id WITH =) WHERE (role = 'owner');
```

### Time-Series Data Handling
```sql
-- Hypertables for time-series data (TimescaleDB)
SELECT create_hypertable('audit_logs', 'created_at');

-- Continuous aggregates for real-time analytics
CREATE MATERIALIZED VIEW hourly_activity
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 hour', created_at) AS hour,
    entity_type,
    COUNT(*) as activity_count
FROM audit_logs
GROUP BY hour, entity_type;
```

### Graph Database Integration
```sql
-- Graph relationships using recursive CTEs
WITH RECURSIVE task_hierarchy AS (
    SELECT id, title, project_id, 0 as level
    FROM tasks 
    WHERE id = $1
    
    UNION ALL
    
    SELECT t.id, t.title, t.project_id, th.level + 1
    FROM tasks t
    JOIN task_dependencies td ON t.id = td.depends_on_task_id
    JOIN task_hierarchy th ON td.task_id = th.id
)
SELECT * FROM task_hierarchy;
```

## Testing and Validation

### Data Model Testing
```sql
-- Test data integrity constraints
DO $$
BEGIN
    -- Test email uniqueness
    INSERT INTO users (email, first_name, last_name, password_hash) 
    VALUES ('test@example.com', 'Test', 'User', 'hash123');
    
    -- This should fail
    BEGIN
        INSERT INTO users (email, first_name, last_name, password_hash) 
        VALUES ('test@example.com', 'Another', 'User', 'hash456');
        RAISE EXCEPTION 'Duplicate email constraint failed';
    EXCEPTION
        WHEN unique_violation THEN
            RAISE NOTICE 'Email uniqueness constraint working correctly';
    END;
END $$;
```

### Performance Testing
```sql
-- Query performance analysis
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT 
    u.email,
    COUNT(t.id) as task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.assigned_to
WHERE u.status = 'active'
GROUP BY u.id, u.email
ORDER BY task_count DESC
LIMIT 10;
```

## Documentation Standards

### ERD Best Practices
- Use consistent naming conventions
- Include cardinality and participation constraints
- Group related entities visually
- Use colors to distinguish entity types
- Include attribute data types and constraints

### SQL Documentation
- Comment all tables, columns, and constraints
- Use descriptive names for indexes and constraints
- Include business rule explanations
- Document performance considerations
- Provide usage examples

### Change Management
- Version all schema changes
- Document migration procedures
- Test rollback scenarios
- Communicate changes to stakeholders
- Update documentation immediately

## Maintenance and Evolution

### Regular Reviews
- Monthly schema review meetings
- Quarterly performance analysis
- Annual security audit
- Continuous compliance monitoring

### Automation
- Automated schema validation
- Performance monitoring alerts
- Data quality dashboards
- Backup verification

### Future Considerations
- Cloud migration strategies
- Microservices decomposition
- Event sourcing implementation
- CQRS pattern adoption

---

**Playbook Version:** 2.0 - Enhanced with 2025 Best Practices  
**Last Updated:** 2025-01-15  
**Compatibility:** Modern databases, cloud platforms, compliance frameworks  
**Review Cycle:** Quarterly or with major technology changes